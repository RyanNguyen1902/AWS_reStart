---
title : "Chuẩn bị tạo AWS CloudFormation stack"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 2.1 </b> "
---

{{% notice info %}}
Sau khi đăng ký tài khoản AWS, bạn cần triển khai AWS CloudFormation stack bằng cách làm theo các bước sau.
{{% /notice %}}

Để tìm hiểu về AMAZON S3 và AWS CLOUDFORMATION các bạn có thể tham khảo bài lab :
  - [AWS CLOUDFORMATION](https://000037.awsstudygroup.com/vi/)
  - [Bắt đầu với AMAZON S3](https://000057.awsstudygroup.com/vi/)


1. Tải xuống và lưu [AWS CloudFormation template](https://github.com/RyanNguyen1902/AWS_reStart/blob/d0ad7895601cc588fcf2fafd1cfc3430505e9dae/Workshop/anomaly-detection-cfn.json/) vào máy tính của bạn.

2. Tải xuống và lưu [anomaly-detection-lambda.zip](https://github.com/RyanNguyen1902/AWS_reStart/blob/d0ad7895601cc588fcf2fafd1cfc3430505e9dae/Workshop/anomaly-detection-lambda.zip/) Lambda code vào máy tính của bạn.

3. Sau khi bạn đã đăng nhập vào Bảng Management Console, chúng ta tạo Amazon S3 với tên bạn chọn. Bạn sẽ cần tạo S3 bucket này trong cùng khu vực mà bạn định triển khai mẫu CloudFormation. Sau khi bạn tạo bucket, hãy tải tệp **“anomaly-detection-lambda.zip”** lên bucket mới tạo. Ảnh chụp màn hình này cho thấy một Amazon S3 bucket có tên là **“ebs-anomaly-detection-bucket”** với mã Lambda nén được tải lên nó.

![ConnectPrivate](/images/2.prerequisite/001-S3-Bucket.png) 


### Nội dung
  - [Tạo VPC](2.1.1-createvpc/)
  - [Tạo Public subnet](2.1.2-createpublicsubnet/)
  - [Tạo Private subnet](2.1.3-createprivatesubnet/)
  - [Tạo security group](2.1.4-createsecgroup/)
  - [Tạo máy chủ Linux public](2.1.5-createec2linux/)
  - [Tạo máy chủ Windows private](2.1.6-createec2windows/)
