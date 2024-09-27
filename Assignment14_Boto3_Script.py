import boto3
import json

def lambda_handler(event, context):
    sns_client = boto3.client('sns')
    topic_arn = 'arn:aws:sns:your-region:your-account-id:your-topic-name'
    
    # Extract details from the event
    detail = event['detail']
    instance_id = detail['instance-id']
    state = detail['state']
    
    # Create the message
    message = f"EC2 Instance {instance_id} is now {state}."
    
    # Send the SNS notification
    sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject='EC2 Instance State Change'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully')
    }
