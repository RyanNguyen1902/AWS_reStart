---
title : "AWS Lambda"
date :  "`r Sys.Date()`" 
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---


Selecting the **Target Name** link directs you to the AWS Lambda function.

![Lambda](/images/5.Lambda/001-Lambda.PNG?featherlight=false&width=90pc)

While the name of your AWS Lambda function will be slightly different, you’ll see the same configuration identifying Amazon EventBridge as the trigger for invoking the function. Explore the code to see how snapshots are compared and how integrations work with both Amazon DynamoDB and Amazon CloudWatch.

The path through the AWS Lambda function is to first check to see if there has already been a backup for the Amazon EBS volume. If this is the first backup, an Amazon CloudWatch alarm, with its name based off the EBS volume ARN, is created. The alarm is created with anomaly detection activated, and a threshold breach is triggered from an Amazon CloudWatch custom metric, also created within this same AWS Lambda function.

If this isn’t the EBS volume’s first backup, the current snapshot is compared against the previous snapshot. To compare the snapshots, the EBS API [ListChangedBlocks](https://docs.aws.amazon.com/ebs/latest/APIReference/API_ListChangedBlocks.html) is invoked to calculate the total number of changed blocks existing between the snapshots. The total number of changed blocks is then added to an Amazon CloudWatch custom metric. Again, this metric will be used to trigger the Amazon CloudWatch alarm that was initially created upon the EBS volume’s first backup.

