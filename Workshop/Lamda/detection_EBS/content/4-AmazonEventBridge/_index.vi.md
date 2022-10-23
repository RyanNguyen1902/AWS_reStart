---
title : "Amazon EventBridge"
date :  "`r Sys.Date()`" 
weight : 4 
chapter : false
pre : " <b> 4. </b> "
---


1. Như được tham chiếu trong ảnh chụp screenshot, ta truy cập trang tổng quan Amazon EventBridge và chọn liên kết **Rules** trong ngăn điều hướng bên trái. Quy tắc(rule) được tạo trong quá trình triển khai AWS CloudFormation sẽ được tìm thấy trong **default** event bus và sẽ được đặt tên tương tự như những gì bạn thấy ở đây.

![Amazon EventBridge](/images/4.AmazonEventBridge/001-EventBridge-Dashboard.png)

Chọn quy tắc(rule) để xem **Event pattern** được xác định cho quy tắc đó. Event pattern này được sử dụng để khớp với các sự kiện events đến được xuất bản từ AWS Backup. Trong mô hình này, bạn sẽ nhận thấy rằng tất cả các bản sao lưu Amazon EBS đã hoàn thành sẽ được khớp với nhau.

![EventPattern](/images/4.AmazonEventBridge/002-EventBridge-Rule-Pattern.png)

   + Chọn **Targets** tab để AWS Lambda function được liên kết được kích hoạt khi quy tắc khớp với một sự kiện sắp tới.

2. + Chọn **Target Name** liên kết để truy cập AWS Lambda function

![EventRuleTarget](/images/4.AmazonEventBridge/003-EventBridge-Rule-Target.png)

