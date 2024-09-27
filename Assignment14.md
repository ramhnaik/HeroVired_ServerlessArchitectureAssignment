## Task: Set up a Lambda function that listens to EC2 state change events and sends SNS notifications detailing the state changes.

## Steps:

### 1. SNS Setup
* Create a New Topic: Go to the SNS dashboard and create a new topic.
* Subscribe to the Topic: Subscribe to this topic with your email to receive notifications.

### 2. Lambda IAM Role
* Create a New Role: In the IAM dashboard, create a new role for Lambda.
* Attach Policies: Attach policies that allow reading EC2 instance states and sending SNS notifications. You can use AmazonEC2ReadOnlyAccess and AmazonSNSFullAccess policies.

### 3. Lambda Function
* Create a New Function: Navigate to the Lambda dashboard and create a new function. Choose Python 3.x as the runtime.
* Assign IAM Role: Assign the IAM role created in the previous step.
  
In the Lambda function code editor, copy and paste [Assignment14_Boto3_Script.py](Assignment14_Boto3_Script.py)


### 4. EC2 EventBridge (formerly CloudWatch Events)
* Create an EventBridge Rule: Go to the EventBridge dashboard and create a new rule.
* Set Event Source: Set the event source to EC2 instance state changes.
* Target: Set the target to the Lambda function you created.

### 5. Testing
* Start or Stop an EC2 Instance: Start or stop one of your EC2 instances.
* Verify: Confirm you receive an SNS notification about the state change.
