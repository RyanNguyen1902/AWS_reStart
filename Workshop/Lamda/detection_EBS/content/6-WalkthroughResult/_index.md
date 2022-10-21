+++
title = "Walkthrough-Result"
date = 2022
weight = 6
chapter = false
pre = "<b>6. </b>"
+++


#### Time to see the solution in action.

Time to see the solution in action.

## AWS Backup

1. To see the solution in action, you’ll need to create some backups for an Amazon EBS volume. If you don’t mind waiting, the AWS Backup plan will kick off the first daily backups tomorrow. But if you want to see the pipeline in action right now, you can navigate over to the AWS Backup dashboard, and within the **On-demand backup** section, 
   + Select the **Create on-demand backup** button.

![Backup-Dashboard](/images/6.WalkthroughResult/001-Backup-Dashboard.png)

2. At this point, you’ll be presented with a screen allowing you to create a backup.

![Backup-On-Demand](/images/6.WalkthroughResult/002-Backup-On-Demand.png)

   For the **Resource type**, select EBS. For the **Volume ID**, select an existing EBS volume to backup. For the purpose of this walkthrough, selecting a smaller volume will result in a quicker backup time. If you don’t have an existing EBS volume, the simplest way to create one is to simply launch an Amazon Elastic Compute Cloud (Amazon EC2) instance. Once the instance is launched, its Volume ID will show up in the list after the screen has been refreshed.

   After selecting these two items, click the **Create on-demand backup** button at the bottom of the screen to start the backup. The backup will start, and you’ll be notified of its status. Initially, t*he backup will be listed as **Created** and then will eventually move to **Completed**. You’ll need to refresh the backup jobs screen to get the updated status. Once in the Completed state, AWS Backup will publish an event to Amazon EventBridge, and the pipeline will be off and running!

## Amazon CloudWatch

3. Now that you’ve started your first backup, it’s time to take a look in **Amazon CloudWatch** to see what’s happening. Navigate to the Amazon CloudWatch dashboard and select the **All alarms** link in the left navigation pane. It might take some time for the AWS Backup event to travel completely through the pipeline, but soon you’ll see a new alarm with a name similar to what’s shown here.

![CloudWatch-Dashboard](/images/6.WalkthroughResult/003-CloudWatch-Dashboard.png)

The alarm was created by the AWS Lambda function we deployed, and it’s configured to detect anomalies based on the Amazon CloudWatch custom metric that will be sent during subsequent backups.

4. If you click on the newly created alarm link, you’ll be taken to a screen which shows the alarm’s details.

![CloudWatch-Alarm-Empty](/images/6.WalkthroughResult/004-CloudWatch-Alarm-Empty.png)

At this point, we don’t have any metric data, so the alarm displays **insufficient data**. In fact, for the Amazon CloudWatch anomaly detection model to be properly trained, we’ll need to go through quite a few backups iterations before a pattern can be established.

Jumping ahead on those additional backups, here’s what you can expect to see once the model has been adequately trained.


1. Go to [EC2 service management console](https://console.aws.amazon.com/ec2/v2/home)
   + Click **Instances**.
   + Select both **Public Linux Instance** and **Private Windows Instance** instances.
   + Click **Instance state**.
   + Click **Terminate instance**, then click **Terminate** to confirm.

2. Go to [IAM service management console](https://console.aws.amazon.com/iamv2/home#/home)
   + Click **Roles**.
   + In the search box, enter **SSM**.
   + Click to select **SSM-Role**.
   + Click **Delete**, then enter the role name **SSM-Role** and click **Delete** to delete the role.

![Clean](/images/6.clean/001-clean.png)

3. Click **Users**.
   + Click on user **Portfwd**.
   + Click **Delete**, then enter the user name **Portfwd** and click **Delete** to delete the user.

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

![Clean](/images/6.clean/002-clean.png)

4. Enter the name of the S3 bucket, then click **Delete bucket** to proceed with deleting the S3 bucket.

![Clean](/images/6.clean/003-clean.png)

#### Delete VPC Endpoints

1. Go to [VPC service management console](https://console.aws.amazon.com/vpc/home)
   + Click **Endpoints**.
   + Select the 4 endpoints we created for the lab including **SSM**, **SSMMESSAGES**, **EC2MESSAGES**, **S3GW**.
   + Click **Actions**.
   + Click **Delete VPC endpoints**.

![Clean](/images/6.clean/004-clean.png)

2. In the confirm box, enter **delete**.
   + Click **Delete** to proceed with deleting endpoints.

3. Click the refresh icon, check that all endpoints have been deleted before proceeding to the next step.

![Clean](/images/6.clean/005-clean.png)

#### Delete VPC

1. Go to [VPC service management console](https://console.aws.amazon.com/vpc/home)
   + Click **Your VPCs**.
   + Click on **Lab VPC**.
   + Click **Actions**.
   + Click **Delete VPC**.

2. In the confirm box, enter **delete** to confirm, click **Delete** to delete **Lab VPC** and related resources.

![Clean](/images/6.clean/006-clean.png)