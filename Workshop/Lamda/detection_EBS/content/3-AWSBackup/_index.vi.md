---
title : "AWS Backup Backup"
date :  "`r Sys.Date()`" 
weight : 3 
chapter : false
pre : " <b> 3. </b> "
---

### AWS Backup Backup

Sau khi bạn đã đăng nhập vào [AWS Management console](https://console.aws.amazon.com/backup/home), đến trang tổng quan AWS Backup dashboard để xem các tài nguyên được tạo trong quá trình triển khai AWS CloudFormation. Trong tab điều hướng bên trái, nhấp vào liên kết **Backup vaults** link. Bạn sẽ thấy một trang tương tự như những gì được hiển thị trong hình này:

**AnomalyDetectionAnomalyDetectionBackupPlanVault**
![Backup-Vaults](/images/3.AWSBackup/001-Backup-Vaults.png) 


1. Backup vault này là một vùng chứa lưu trữ và tổ chức các bản sao lưu được liên kết với các ổ Amazon EBS khớp với khóa tag key mà bạn đã nhập cho thông số **AnomalyDetectionTagKey** AWS CloudFormation.
+ Tiếp theo, chọn **Backup plans** link trong tab hướng bên trái để truy cập backup plan được tạo trong quá trình triển khai.

![Backup-Plan](/images/3.AWSBackup/002-Backup-Plan.png) 

2. Chọn **AnomalyDetectionBackupPlan** link dưới “Backup plan name” để truy cập thông tin chi tiết.

![Backup-Plan](/images/3.AWSBackup/003-Backup-Plan.png) 

CloudFormation mặc định tạo quy tắc sao lưu hàng ngày và hàng tháng với thời gian lưu giữ 1 năm. Nếu mặc định này không phù hợp với yêu cầu của bạn, vui lòng xóa / thêm các quy tắc mới nếu bạn thấy phù hợp.

Gán tài nguyên **Selection** chọn các tài nguyên EBS khớp với thông số khóa tag key mà bạn đã nhập trong quá trình triển khai. Giống như các quy tắc sao lưu, nếu việc chỉ định tài nguyên mặc định không phù hợp với nhu cầu của bạn, bạn có thể xóa và chỉ định một tài nguyên mới.
