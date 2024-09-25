# Using AWS Lambda and Boto3 , automate the stopping and starting of EC2 instances based on tags.

## Steps:

### 1. EC2 Setup:
##### Create EC2 Instances:
* Navigate to the EC2 dashboard in the AWS Management Console.
* Launch two new t2.micro instances.
* Tag the first instance with a key Action and value Auto-Stop.
* Tag the second instance with a key Action and value Auto-Start.

### 2. Lambda IAM Role
#### Create IAM Role:
* Go to the IAM dashboard.
* Create a new role with the following settings:
  - Trusted entity: AWS service
  - Use case: Lambda
* Attach the AmazonEC2FullAccess policy to this role.
  
### 3. Lambda Function
#### Create Lambda Function:
* Navigate to the Lambda dashboard.
* Create a new function with the following settings:
  - Runtime: Python 3.x
  - Role: Use the IAM role created in the previous step.
#### Write the Boto3 Script:
In the Lambda function code editor, copy and paste Assignment1_Boto3_Script.py script

### 4. Manual Invocation
#### Invoke the Lambda Function:
* Save Lambda function created.
* Manually trigger the function from the Lambda dashboard.
#### Verify EC2 Instances:
* Go to the EC2 dashboard.
* Confirm that the instance tagged Auto-Stop has stopped and the one tagged Auto-Start has started.
