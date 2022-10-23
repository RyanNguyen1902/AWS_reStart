---
title : "Preparation "
date : "`r Sys.Date()`"
weight : 2
chapter : false
pre : " <b> 2. </b> "
---

{{% notice info %}}
Once you’ve signed up for an AWS account, you can deploy the AWS CloudFormation stack by following these steps.
{{% /notice %}}

The architecture overview after you complete this step will be as follows:


To learn about AMAZON S3 and AWS CLOUDFORMATION you can refer to the lab:
  - [AWS CLOUDFORMATION](https://000037.awsstudygroup.com/)
  - [Starting with Amazon S3](https://000057.awsstudygroup.com/)

1. Download and save the [AWS CloudFormation template](https://github.com/RyanNguyen1902/AWS_reStart/blob/d0ad7895601cc588fcf2fafd1cfc3430505e9dae/Workshop/anomaly-detection-cfn.json/) to your local computer.

2. Download and save the [anomaly-detection-lambda.zip](https://github.com/RyanNguyen1902/AWS_reStart/blob/d0ad7895601cc588fcf2fafd1cfc3430505e9dae/Workshop/anomaly-detection-lambda.zip/) Lambda code to your local computer.

3. After you’ve logged into the AWS Management Console, create an Amazon S3 bucket with a name you choose. You’ll need to create this S3 bucket in the same region you intend to deploy the CloudFormation template. After you create the bucket, upload the **“anomaly-detection-lambda.zip”** file to the newly created bucket. 

![S3](/images/2.prerequisite/001-s3.png) 

This screenshot shows an Amazon S3 bucket named **“ebs-anomaly-detection-bucket”** with the zipped Lambda code uploaded to it.

![S3-Bucket](/images/2.prerequisite/002-S3-Bucket.png) 

### Content
  - [Create CloudFormation stack](2.1-CloudFormationstack/)
