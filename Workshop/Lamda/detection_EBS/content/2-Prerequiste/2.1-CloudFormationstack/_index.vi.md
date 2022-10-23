---
title : "Chuẩn bị, tạo AWS CloudFormation stack"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 2.1 </b> "
---

#### Tạo AWS CloudFormation stackk
1. Vào [AWS Management console](https://console.aws.amazon.com/cloudformation/home)
Tạo CloudFormation stack bằng cách vào  AWS CloudFormation dashboard. 
![CloudFormation](/images/2.prerequisite/003-CloudFormation.png)

  + Chọn Tải lên tệp **template file** và chọn tệp **“anomaly-Discovery-cfn.json”** - tệp mà bạn đã tải xuống.
  + Click **Next**.

![CloudFormation](/images/2.prerequisite/004-CloudFormation-Create.png)

2. Ở cửa sổ **CloudFormation stack** details, bạn sẽ được yêu cầu cung cấp bốn tham số trong quá trình triển khai:

![CloudFormation](/images/2.prerequisite/005-CloudFormation-Details.png)

  + **AnomalyDetectionEmail**: Địa chỉ email này sẽ nhận thông báo Amazon SNS và sẽ được sử dụng để định cấu hình Amazon SNS topic. Trong quá trình triển khai AWS CloudFormation, bạn sẽ nhận được email tại địa chỉ này, với chủ đề **“AWS Notification – Subscription Confirmation”**, yêu cầu bạn xác nhận đăng ký của mình bằng cách nhấp vào liên kết trong email.
  ![AWSSNS](/images/2.prerequisite/007-AWSSNS.png)

  + **AnomalyDetectionTagKey**: Tag key này sẽ xác định Amazon EBS volumes cần đưa vào để phát hiện sự bất thường. Bất kỳ EBS volume nào có Tag key này được xác định sẽ được chọn bởi Kế hoạch sao lưu AWS được tạo trong quá trình thiết lập AWS CloudFormation.

  + **BackupAnomalyDetectionS3Bucket**: Đây là tên của S3 bucket mà bạn đã tạo ở trước đó. Lưu ý rằng, S3 bucket này cần ở cùng khu vực mà bạn hiện đang triển khai mẫu CloudFormation này.

  + **BackupAnomalyDetectionS3Code**: Đây là tên một ZIP file bạn đã upload lên S3 bucket và trong đó chứa Lambda code.

  + Nhấp vào nút **Next button** và cả ở trang tiếp theo sau (cấu hình các tùy chọn stack).

3. Cuộn xuống cuối màn hình xem lại, chọn kiểm tra ***I acknowledge that AWS CloudFormation might create IAM resources**. 
  + Chọn nút **Create stack** để tạo CloudFormation stack.

![CloudFormation](/images/2.prerequisite/006-CloudFormation-Finish.png)

#### Configuration
  Sau khi bạn khởi chạy xong stack, mọi thứ sẽ được triển khai vào tài khoản AWS của bạn và sau đó bạn có thể sẵn sàng kiểm tra tài nguyên đã tạo.

![CloudFormation-Completed](/images/2.prerequisite/008-CloudFormation-Completed.png)