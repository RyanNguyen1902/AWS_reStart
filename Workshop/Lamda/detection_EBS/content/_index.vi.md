---
title : "AWS Backup anomaly detection for Amazon EBS volumes"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
---
# AWS Backup phát hiện bất thường cho Amazon EBS Volume

### Tổng quan

Bảo vệ dữ liệu của bạn khỏi các cuộc tấn công mạng và ransomware là một phần quan trọng, cần thiết để phát hiện hoạt động bất thường ở mọi cấp trong tổ chức của bạn có thể giúp bạn giữ cho dữ liệu của mình an toàn nhất có thể. Lưu trữ dữ liệu là một lĩnh vực quan trọng mà bạn có thể và nên triển khai tính năng phát hiện bất thường.

  Trong bài này, bạn sẽ học cách bảo vệ bộ nhớ của mình và thực hành xây dựng một đường dẫn đơn giản không có máy chủ(serverless) để phát hiện các điểm bất thường xảy ra trên các  Amazon Elastic Block Store (EBS) volumes. 

![ConnectPrivate](/images/AWS-Backup-Anomaly-Detection.png?featherlight=false&width=90pc) 

### Nội dung

 1. [Giới thiệu](1-introduce/)
 2. [Các bước chuẩn bị](2-Prerequiste/)
 3. [AWS Backup](3-AWSBackup/)
 4. [Amazon Event Bridge](4-AmazonEventBridge/)
 5. [Lambda](5-Lambda/)
 6. [Kiểm tra kết quả](6-WalkthroughResult/)
 7. [Clean up resources](7-cleanup/)

