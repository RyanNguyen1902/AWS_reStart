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

![ConnectPrivate](/images/AWS-Backup-Anomaly-Detection.png) 

### Nội dung

 1. [Giới thiệu](1-introduce/)
 2. [Các bước chuẩn bị](2-Prerequiste/)
 3. [Tạo kết nối đến máy chủ EC2](3-Accessibilitytoinstance/)
 4. [Quản lý session logs](4-s3log/)
 5. [Port Forwarding](5-Portfwd/)
 6. [Dọn dẹp tài nguyên](6-cleanup/)

