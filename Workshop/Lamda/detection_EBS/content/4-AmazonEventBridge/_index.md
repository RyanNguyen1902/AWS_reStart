---
title : "Amazon EventBridge"
date : "`r Sys.Date()`"
weight : 4
chapter : false
pre : " <b> 4. </b> "
---


1. As referenced in the following screenshot, go to the Amazon EventBridge dashboard and select the **Rules** link in the left navigation pane. The rule created during the AWS CloudFormation deployment will be found under the **default** event bus and will be named something similar to what you see here.

![Amazon EventBridge](/images/4.AmazonEventBridge/001-EventBridge-Dashboard.PNG?featherlight=false&width=90pc)

Select the rule to see the **Event pattern** defined for it. This event pattern is used to match incoming events published from AWS Backup. In this pattern, you’ll notice that all completed Amazon EBS backups will be matched.

![EventPattern](/images/4.AmazonEventBridge/002-EventBridge-Rule-Pattern.PNG?featherlight=false&width=90pc)

   + Select the **Targets** tab to see the associated AWS Lambda function that’s triggered when the rule matches an incoming event.

2. + Select the **Target Name** link to access the AWS Lambda function

![EventRuleTarget](/images/4.AmazonEventBridge/003-EventBridge-Rule-Target.PNG?featherlight=false&width=90pc)

