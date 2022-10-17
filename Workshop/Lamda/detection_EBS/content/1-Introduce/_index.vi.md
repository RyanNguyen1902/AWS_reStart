---
title : "Giới thiệu"
date :  "`r Sys.Date()`" 
weight : 1 
chapter : false
pre : " <b> 1. </b> "
---
Giải pháp ở đây là **AWS Backup**. Khi Amazon EBS volume được sao lưu, một ảnh chụp nhanh(snapshot) sẽ được tạo. Bằng cách so sánh ảnh chụp nhanh hiện tại này với ảnh chụp nhanh đã tạo trước đó, có thể dễ dàng xác định số lượng khối(block) đã thay đổi giữa hai khối. Giá trị của khối đã thay đổi này được đẩy lên **Amazon CloudWatch** dưới dạng chỉ số tùy chỉnh, trong đó cảnh báo của Amazon CloudWatch được định cấu hình để **phát hiện sự bất thường** trên chỉ số. Bằng cách sử dụng khả năng học máy mạnh mẽ được tích hợp sẵn của Amazon CloudWatch, các điểm bất thường sẽ được phát hiện và hiển thị khi phạm vi ngưỡng của cảnh báo. Khi điều này xảy ra, mọi thông báo cảnh báo được định cấu hình trước sẽ được kích hoạt.

Để xây dựng hệ thống phát hiện bất thường, chúng ta sử dụng các dịch vụ sau:

- AWS Backup: Chúng ta sẽ sử dụng AWS Backup để quản lý các bản sao lưu của Amazon EBS volumes. Đối lab này, chúng ta sẽ tạo một kế hoạch dự phòng chọn các  EBS volumes dựa trên tag key mà bạn cung cấp trong quá trình thiết lập. Sau khi bắt đầu sao lưu, một ảnh chụp(snapshot) nhanh sẽ được tạo và các sự kiện từ quy trình Sao lưu AWS được xuất lên Amazon EventBridge.
- Amazon EventBridge: Amazon EventBridge là một serverless event bus và nó nhận các event đến từ AWS Backup. Đối với các event sao lưu khớp với quy tắc được định cấu hình trước mà chúng ta tạo thì EventBridge sẽ kích hoạt một hàm AWS Lambda.
- AWS Lambda: Tất cả các AWS Backup events khớp với quy tắc Amazon EventBridge được chuyển đến AWS Lambda , hàm AWS Lambda trích xuất Amazon EBS volume Amazon Resource Name (ARN) và tên ảnh chụp nhanh(snapshot) hiện tại. Sử dụng ARN làm key, chi tiết ảnh chụp nhanh(snapshot) sao lưu trước đó được truy xuất từ ​​bảng Amazon DynamoDB. Nếu mục ảnh chụp nhanh(snapshot) trước đó được tìm thấy ARN đã cho thì ảnh chụp(snapshot) nhanh hiện tại và trước đó được so sánh để thay đổi. Giá trị thay đổi được tính toán được chuyển cùng với Amazon CloudWatch dưới dạng chỉ số tùy chỉnh. Nếu mục ảnh chụp nhanh(snapshot) trước đó không được tìm thấy trong bảng Amazon DynamoDB, một mục mới sẽ được tạo và cảnh báo Amazon CloudWatch được định cấu hình cho ARN.
- Amazon DynamoDB: Đối với mỗi event sao lưu đến với hàm AWS Lambda, một bảng Amazon DynamoDB được sử dụng để lưu giữ thông tin chi tiết về event. ARN từ event được sử dụng làm khóa phân vùng và tên ảnh chụp nhanh(snapshot) được đính kèm làm thuộc tính cho mục.
- Amazon CloudWatch: Chỉ số tùy chỉnh được tạo trong hàm AWS Lambda và được gửi đến Amazon CloudWatch. Giá trị số liệu chứa số lượng blocks đã thay đổi giữa ảnh chụp nhanh hiện tại(snapshot) và ảnh chụp(snapshot) trước đó. Một cảnh báo CloudWatch, đã được định cấu hình và tạo trước đó trong chức năng AWS Lambda, được kích hoạt khi dải ngưỡng phát hiện bất thường .
- Amazon Simple Notification Service (Amazon SNS): Khi cảnh báo CloudWatch được kích hoạt, Amazon SNS sẽ gửi thông báo đến địa chỉ email được định cấu hình trong quá trình thiết lập.
  
Sơ đồ sau minh họa kiến trúc của giải pháp::
![ConnectPrivate](/images/AWS-Backup-Anomaly-Detection.png) 