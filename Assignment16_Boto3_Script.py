Python

import boto3
import json
import paramiko

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    sns_client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:your-region:your-account-id:your-topic-name'
    
    # Describe EC2 instances
    instances = ec2_client.describe_instances()
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            public_ip = instance['PublicIpAddress']
            
            # Connect to the instance using SSH
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(public_ip, username='ec2-user', key_filename='/path/to/your/key.pem')
            
            # Execute the command to check disk space
            stdin, stdout, stderr = ssh.exec_command('df -h /')
            output = stdout.read().decode('utf-8')
            
            # Parse the output to get the disk utilization percentage
            lines = output.split('\n')
            if len(lines) > 1:
                disk_usage = lines[1].split()[4]
                disk_usage_percent = int(disk_usage.strip('%'))
                
                # Check if disk usage exceeds 85%
                if disk_usage_percent > 85:
                    message = f"EC2 Instance {instance_id} has exceeded disk usage threshold with {disk_usage_percent}% utilization."
                    sns_client.publish(
                        TopicArn=topic_arn,
                        Message=message,
                        Subject='EC2 Disk Space Alert'
                    )
            
            ssh.close()
    
    return {
        'statusCode': 200,
        'body': json.dumps('Disk space check complete')
    }
