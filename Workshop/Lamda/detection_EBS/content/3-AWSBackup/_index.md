---
title : "AWS Backup"
date : "`r Sys.Date()`"
weight : 3
chapter : false
pre : " <b> 3. </b> "
---

### AWS Backup Backup

After you’ve logged into the AWS Management Console, navigate to the AWS Backup dashboard to look at the resources created during the AWS CloudFormation deployment. In the left navigation pane, click on the **Backup vaults** link. You should see something similar to what’s shown in this figure, with a newly created vault called

**AnomalyDetectionAnomalyDetectionBackupPlanVault**
![Backup-Vaults](/images/3.AWSBackup/001-Backup-Vaults.png) 


1. This backup vault is a container that stores and organizes backups associated with the Amazon EBS volumes that match the tag key you entered for the **AnomalyDetectionTagKey** AWS CloudFormation parameter.

+ Next, select the **Backup plans** link in the left navigation pane to access the backup plan created during the deployment.

2. Select the **AnomalyDetectionBackupPlan** link under “Backup plan name” to access detailed information.

![Backup-Plan](/images/3.AWSBackup/002-Backup-Plan.png) 

The default CloudFormation creates daily and monthly backup rules with 1-year retention. If this default doesn’t match your requirements, feel free to delete/add new rules as you see fit.

The **Selection** resource assignment selects EBS resources matching the tag key parameter you entered during deployment. Like backup rules, if the default resource assignment doesn’t fit your needs, you can delete and assign a new one.

### Content
3.1. [Connect to EC2 Public Server](3.1-public-instance/)
3.2. [Cconnect to EC2 Private Server](3.2-private-instance/)