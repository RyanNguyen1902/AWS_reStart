+++
title = "Clean up resources"
date = 2022
weight = 7
chapter = false
pre = "<b>7. </b>"
+++

We will take the following steps to delete the resources we created in this exercise.

#### Delete a stack on the AWS CloudFormation console

1. Go to [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/) page
2. In the **CloudFormation** interface, select **Stack**
3. Select Stack to delete
4. Select **Delete**
5. Verify clearing stack
6. Wait a few minutes for the stack to change state to **DELETE_COMPLETE** to be deleted successfully

![AWS CloudFormation](/images/7.clean/001-clean.PNG)

#### Delete S3 bucket

1. Access [System Manager - Session Manager service management console](https://console.aws.amazon.com/systems-manager/session-manager).
   + Click the **Preferences** tab.
   + Click **Edit**.
   + Scroll down.
   + In the section **S3 logging**.
   + Uncheck **Enable** to disable logging.
   + Scroll down.
   + Click **Save**.

2. Go to [S3 service management console](https://s3.console.aws.amazon.com/s3/home)
   + Click on the S3 bucket we created for this lab. (Example: lab-fcj-bucket-0001 )
   + Click **Empty**.
   + Enter **permanently delete**, then click **Empty** to proceed to delete the object in the bucket.
   + Click **Exit**.

3. After deleting all objects in the bucket, click **Delete**

![Clean](/images/7.clean/003-clean.PNG)

4. Enter the name of the S3 bucket, then click **Delete bucket** to proceed with deleting the S3 bucket.

![Clean](/images/7.clean/004-clean.PNG)

#### Delete EC2 instance

1. Go to [EC2 service management console](https://console.aws.amazon.com/ec2/v2/home)
   + Click **Instances**.
   + Select both **Public Linux Instance** and **Private Windows Instance** instances.
   + Click **Instance state**.
   + Click **Terminate instance**, then click **Terminate** to confirm.

   ![AWS EC2](/images/7.clean/002-clean.PNG)