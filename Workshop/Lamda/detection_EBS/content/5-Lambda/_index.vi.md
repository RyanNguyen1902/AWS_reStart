---
title : "AWS Lambda"
date :  "`r Sys.Date()`" 
weight : 5 
chapter : false
pre : " <b> 5. </b> "
---


Chọn **Target Name** liên kết sẽ đưa bạn đến AWS Lambda function.

![Lambda](/images/5.Lambda/001-Lambda.PNG?featherlight=false&width=90pc)

Mặc dù tên của hàm AWS Lambda của bạn sẽ hơi khác một chút, nhưng bạn sẽ thấy cùng một cấu hình xác định Amazon EventBridge làm trình kích hoạt để gọi hàm. Chúng ta có thể xem code để xem ảnh chụp nhanh snapshots được so sánh như thế nào và cách tích hợp hoạt động với cả **Amazon DynamoDB và Amazon CloudWatch**.

Đường dẫn thông qua AWS Lambda function trước tiên là để kiểm tra xem đã có bản sao lưu cho Amazon EBS volume chưa. Nếu đây là bản sao lưu đầu tiên, một cảnh báo **Amazon CloudWatch**, với tên dựa trên ARN Amazon EBS volume, sẽ được tạo. Cảnh báo được tạo khi kích hoạt tính năng phát hiện bất thường và vi phạm ngưỡng được kích hoạt từ chỉ số tùy chỉnh Amazon CloudWatch, cũng được tạo trong cùng chức năng AWS Lambda này.

Nếu đây không phải là bản sao lưu đầu tiên của EBS volume, thì ảnh chụp nhanh hiện tại snapshot  sẽ được so sánh với ảnh chụp nhanh trước đó. Để so sánh các ảnh chụp nhanh snapshots, EBS API [ListChangedBlocks](https://docs.aws.amazon.com/ebs/latest/APIReference/API_ListChangedBlocks.html) được gọi để tính tổng số blocks đã thay đổi hiện có giữa các ảnh chụp nhanh snapshot . Sau đó, tổng số số blocks đã thay đổi được thêm vào chỉ số tùy chỉnh của Amazon CloudWatch. Một lần nữa, chỉ số này sẽ được sử dụng để kích hoạt cảnh báo Amazon CloudWatch được tạo ban đầu khi sao lưu đầu tiên của EBS volume.
