import boto3

def lambda_handler(event, context):
    # Initialize EC2 client
    ec2 = boto3.client('ec2')
    
    # Get all EC2 instances
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Action',  # Filter by tag key
                'Values': ['Ramananda-Auto-Stop', 'Ramananda-Auto-Start']  # Filter by tag values
            }
        ]
    )
    
    # Initialize empty lists to store instance IDs for starting/stopping
    to_start = []
    to_stop = []
    
    # Loop through the instances and sort them based on their tags
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            action = next((tag['Value'] for tag in instance['Tags'] if tag['Key'] == 'Action'), None)
            
            if action == 'Ramananda-Auto-Stop':
                to_stop.append(instance_id)
            elif action == 'Ramananda-Auto-Start':
                to_start.append(instance_id)
    
    # Start instances with 'Ramananda-Auto-Start' tag
    if to_start:
        ec2.start_instances(InstanceIds=to_start)
        print(f'Started instances: {to_start}')
    
    # Stop instances with 'Ramananda-Auto-Stop' tag
    if to_stop:
        ec2.stop_instances(InstanceIds=to_stop)
        print(f'Stopped instances: {to_stop}')
    
    return {
        'statusCode': 200,
        'body': f'Started instances: {to_start}, Stopped instances: {to_stop}'
    }
