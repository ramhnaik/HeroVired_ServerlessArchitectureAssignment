## Task: Automate the deletion of files older than 30 days in a specific S3 bucket

## Steps: 

### 1. S3 Setup
* Create a New Bucket: Go to the S3 dashboard and create a new bucket.
* Upload Files: Upload multiple files to this bucket, ensuring some are older than 30 days. You can adjust your system’s date temporarily or use old files.

### 2. Lambda IAM Role
* Create a New Role: In the IAM dashboard, create a new role for Lambda.
* Attach Policy: Attach the AmazonS3FullAccess policy to this role. For real-world scenarios, consider using more restrictive permissions.

### 3. Lambda Function
* Create a New Function: Navigate to the Lambda dashboard and create a new function. Choose Python 3.x as the runtime.
* Assign IAM Role: Assign the IAM role created in the previous step.
  In the Lambda function code editor, copy and paste [Assignment2_Boto3_Script.py](Assignment2_Boto3_Script.py)

### 4. Manual Invocation
* Save and Test: Save your function and manually trigger it.
* Verify: Go to the S3 dashboard and confirm that only files newer than 30 days remain
