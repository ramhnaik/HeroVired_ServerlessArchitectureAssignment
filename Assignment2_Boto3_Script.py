import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'ramananda_s3_bucket'
    days_old = 30
    delete_older_than = datetime.now(timezone.utc) - timedelta(days=days_old)

    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            if obj['LastModified'] < delete_older_than:
                print(f"Deleting {obj['Key']}")
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
    return {
        'statusCode': 200,
        'body': 'Cleanup complete'
    }
