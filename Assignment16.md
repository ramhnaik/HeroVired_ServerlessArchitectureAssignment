## Task : Set up a Lambda function that checks EC2 instances for disk space utilization, sending an SNS alert if utilization exceeds 85%.

## Steps:

### 1. Create a Lambda Function
* Navigate to the Lambda Dashboard: Create a new function and choose Python 3.x as the runtime.
* Assign IAM Role: Ensure the role has permissions to describe EC2 instances and publish to SNS. Attach AmazonEC2ReadOnlyAccess and AmazonSNSFullAccess policies.

### 2. Write the Boto3 Script
* Script to Check Disk Space Utilization:
[Assignment16_Boto3_Script.py](Assignment16_Boto3_Script.py)


### 3. Set Up CloudWatch Event
* Create a Rule: Go to the CloudWatch dashboard and create a new rule.
* Event Source: Set the event source to a schedule (e.g., daily).
* Target: Set the target to the Lambda function you created.

### 4. Testing
* Deploy and Test: Deploy your Lambda function and manually trigger it to ensure it works as expected.
* Verify: Check your email for SNS notifications if any instance exceeds the disk space threshold.
