---
title : "Preparing AWS CloudFormation stack"
date : "`r Sys.Date()`"
weight : 1
chapter : false
pre : " <b> 2.1 </b> "
---

#### Create a new CloudFormation stack
1. Go to [AWS Management console](https://console.aws.amazon.com/cloudformation/home)
Create a new CloudFormation stack by using the AWS Management Console from the AWS CloudFormation dashboard. 
![CloudFormation](/images/2.prerequisite/003-CloudFormation.png)

  + Choose Upload a template file as the Template source and Choose file **“anomaly-detection-cfn.json”** – the file you downloaded.
  + Click **Next**.

![CloudFormation](/images/2.prerequisite/004-CloudFormation-Create.png)

2. At the **CloudFormation stack** details, you’ll be asked to provide four parameters during deployment:

![CloudFormation](/images/2.prerequisite/005-CloudFormation-Details.png)

  + **AnomalyDetectionEmail**: This email address will receive Amazon SNS notifications and will be used to configure the Amazon SNS topic. During the AWS CloudFormation deployment, you’ll receive an email at this address, with subject **“AWS Notification – Subscription Confirmation”**, asking you to confirm your subscription by clicking a link within the email.
    ![AWSSNS](/images/2.prerequisite/007-AWSSNS.png)

  + **AnomalyDetectionTagKey**: This tag key will identify Amazon EBS volumes to include for anomaly detection. Any EBS volume with this tag key defined (tag value ignored) will be selected by the AWS Backup Plan created during the AWS CloudFormation setup.

  + **BackupAnomalyDetectionS3Bucket**: This is the name of the S3 bucket you created in Step 3. As a reminder, this S3 bucket needs to be in the same region where you’re currently deploying this CloudFormation template.

  + **BackupAnomalyDetectionS3Code**: This is the name of the ZIP file you uploaded to the S3 bucket  and contains the Lambda code.

  + Click the **Next button** and also on the following screen (configure stack options).

3. Scroll to the bottom of the review screen, check the I acknowledge that AWS CloudFormation might create IAM resources. 
  + Click the **Create stack** button to create the CloudFormation stack.

![CloudFormation](/images/2.prerequisite/006-CloudFormation-Finish.png)


#### Configuration
  Once you’ve finished launching the stack, everything will be deployed to your AWS account, and then you’ll be ready to take a look around.

  ![CloudFormation-Completed](/images/2.prerequisite/008-CloudFormation-Completed.png)