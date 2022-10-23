---
title : "Introduction"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---
At the start of the solution is **AWS Backup**. When an Amazon EBS volume is backed up, a snapshot is created. By comparing this current snapshot to a previously created snapshot, the number of changed blocks between the two can easily be determined. This changed-blocks value is published to **Amazon CloudWatch** as a custom metric, where an Amazon CloudWatch alarm is configured to **detect anomalies** on the metric. By using the powerful built-in machine learning capabilities of Amazon CloudWatch, anomalies are detected and surfaced when the alarm’s threshold band is breached. When this happens, any pre-configured alarm notifications are triggered.

To build the anomaly-detection pipeline, we use the following services:

- **AWS Backup**: We’ll use AWS Backup to manage backups of Amazon EBS volumes. For this post, we’ll create a backup plan which selects EBS volumes based on a tag key you provide during setup. Once a backup starts, a snapshot is created and events from the AWS Backup process are published to Amazon EventBridge.
- **Amazon EventBridge**: Amazon EventBridge is a serverless event bus, and it receives incoming events published from AWS Backup. For backup events that match a preconfigured rule that we create, EventBridge will trigger an AWS Lambda function.
- **AWS Lambda**: All AWS Backup events that match the Amazon EventBridge rule are passed to an AWS Lambda From the event, the AWS Lambda function extracts the Amazon EBS volume Amazon Resource Name (ARN) and the current snapshot name. Using the ARN as a key, the previous backup snapshot details are retrieved from an Amazon DynamoDB table. If a previous snapshot item is found for the given ARN, the current and previous snapshots are compared for change. The calculated change value is passed along to Amazon CloudWatch as a custom metric. If a previous snapshot item was not found in the Amazon DynamoDB table, a new item is created, and an Amazon CloudWatch alarm is configured for the ARN.
- **Amazon DynamoDB**: For each backup event arriving at the AWS Lambda function, an Amazon DynamoDB table is used to persist details about the event. The ARN from the event is used as the partition key, and the snapshot name is attached as an attribute to the item.
- **Amazon CloudWatch**: A custom metric is created in the AWS Lambda function and is sent to Amazon CloudWatch. The metric value contains the number of changed blocks between the current snapshot and the previous. A CloudWatch alarm, that was previously configured and created in the AWS Lambda function, is triggered when the anomaly-detection threshold band is breached.
- **Amazon Simple Notification Service (Amazon SNS)**: When a CloudWatch alarm is triggered, an Amazon SNS topic delivers a notification to the email address configured during setup.
  
The following diagram illustrates the architecture of the solution:
![ConnectPrivate](/images/AWS-Backup-Anomaly-Detection.png) 