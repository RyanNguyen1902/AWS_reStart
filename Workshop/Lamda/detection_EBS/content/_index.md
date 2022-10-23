---
title : "AWS Backup anomaly detection for Amazon EBS volumes"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
---
# AWS Backup anomaly detection for Amazon EBS volumes

### Overall
 Protecting your data from cyberattacks and ransomware is a critical responsibility, and taking the necessary steps to detect anomalous activity at every level within your organization can help you keep your data as safe as possible. Data storage is an important area where you can and should deploy anomaly detection.

 In this lab, you'll learn protect your storage and practice to build a simple serverless pipeline to detect anomalies occurring on Amazon Elastic Block Store (EBS) volumes. I use AWS Backup along with several other AWS managed services to build the solution.. 

![ConnectPrivate](/images/AWS-Backup-Anomaly-Detection.png) 

### Content
 1. [Introduction ](1-introduce/)
 2. [Preparation](2-prerequiste/)
 3. [AWS Backup](3-AWSBackup/)
 4. [Amazon Event Bridge](4-AmazonEventBridge/)
 5. [Lambda](5-Lambda/)
 6. [WalkthroughResult](6-WalkthroughResult/)
 7. [Clean up resources](7-cleanup/)