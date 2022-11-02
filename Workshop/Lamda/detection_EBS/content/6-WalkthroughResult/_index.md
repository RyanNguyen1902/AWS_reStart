+++
title = "Walkthrough-Result"
date = 2022
weight = 6
chapter = false
pre = "<b>6. </b>"
+++


#### Time to see the solution in action.

Time to see the solution in action.

#### AWS Backup

1. To see the solution in action, you’ll need to create some backups for an Amazon EBS volume. If you don’t mind waiting, the AWS Backup plan will kick off the first daily backups tomorrow. But if you want to see the pipeline in action right now, you can navigate over to the AWS Backup dashboard, and within the **On-demand backup** section, 
   + Select the **Create on-demand backup** button.

![Backup-Dashboard](/images/6.WalkthroughResult/001-Backup-Dashboard.png?featherlight=false&width=90pc)

2. At this point, you’ll be presented with a screen allowing you to create a backup.

![Backup-On-Demand](/images/6.WalkthroughResult/002-Backup-On-Demand.png?featherlight=false&width=90pc)

   For the **Resource type**, select EBS. For the **Volume ID**, select an existing EBS volume to backup. For the purpose of this walkthrough, selecting a smaller volume will result in a quicker backup time. If you don’t have an existing EBS volume, the simplest way to create one is to simply launch an Amazon Elastic Compute Cloud (Amazon EC2) instance. Once the instance is launched, its Volume ID will show up in the list after the screen has been refreshed.

   After selecting these two items, click the **Create on-demand backup** button at the bottom of the screen to start the backup. The backup will start, and you’ll be notified of its status. Initially, t*he backup will be listed as **Created** and then will eventually move to **Completed**. You’ll need to refresh the backup jobs screen to get the updated status. Once in the Completed state, AWS Backup will publish an event to Amazon EventBridge, and the pipeline will be off and running!

   ![Backup-EBS](/images/6.WalkthroughResult/007-Backup-ebs.PNG?featherlight=false&width=90pc)

#### Amazon CloudWatch

3. Now that you’ve started your first backup, it’s time to take a look in **Amazon CloudWatch** to see what’s happening. Navigate to the Amazon CloudWatch dashboard and select the **All alarms** link in the left navigation pane. It might take some time for the AWS Backup event to travel completely through the pipeline, but soon you’ll see a new alarm with a name similar to what’s shown here.

![CloudWatch-Dashboard](/images/6.WalkthroughResult/003-CloudWatch-Dashboard.png?featherlight=false&width=90pc)

The alarm was created by the AWS Lambda function we deployed, and it’s configured to detect anomalies based on the Amazon CloudWatch custom metric that will be sent during subsequent backups.

4. If you click on the newly created alarm link, you’ll be taken to a screen which shows the alarm’s details.

![CloudWatch-Alarm-Empty](/images/6.WalkthroughResult/004-CloudWatch-Alarm-Empty.png?featherlight=false&width=90pc)

At this point, we don’t have any metric data, so the alarm displays **insufficient data**. In fact, for the Amazon CloudWatch anomaly detection model to be properly trained, we’ll need to go through quite a few backups iterations before a pattern can be established.

5. Jumping ahead on those additional backups, here’s what you can expect to see once the model has been adequately trained.

![CloudWatch-Alarm-Populated](/images/6.WalkthroughResult/005-CloudWatch-Alarm-Populated.png?featherlight=false&width=90pc)

Checking now, a substantial number of backups have taken place, and you’ll notice a gray band stretching across the display. This is the anomaly-detection band, and when current and previous snapshots are compared and have too many changed blocks, the grey-band threshold is broken and the alarm is triggered.

6. Finally, let’s take a look at the actual Amazon CloudWatch custom metric. If you click on the **View in metrics** button in the upper-right section of the graph, you’ll be directed to the metrics page, where you can see all metric data points and also the metric and its anomaly-detection configuration.

![CloudWatch-Alarm-Populated](/images/6.WalkthroughResult/006-CloudWatch-Metrics.png?featherlight=false&width=90pc)

#### Conclusion

Detecting anomalies within your data is an important way to stay ahead of cyberattacks and ransomware. In this blog post, I walked through building a simple serverless anomaly-detection pipeline using native services in AWS to identify anomalies within Amazon EBS Volumes during backup. By using the powerful built-in machine learning capabilities of Amazon CloudWatch, anomalous activity is surfaced, and you’re alerted when snapshot backup sizes breach a threshold band. This allows you to keep an ever-watchful eye on your important data.

