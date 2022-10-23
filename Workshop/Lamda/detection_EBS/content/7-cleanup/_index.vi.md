+++
title = "Dọn dẹp tài nguyên  "
date = 2021
weight = 7
chapter = false
pre = "<b>7. </b>"
+++

Chúng ta sẽ tiến hành các bước sau để xóa các tài nguyên chúng ta đã tạo trong bài thực hành này.

#### Delete a stack on the AWS CloudFormation console

1. Truy cập vào trang [AWS CloudFormation](https://console.aws.amazon.com/cloudformation/)
2. Trong giao diện **CloudFormation** chọn Stack
3. Chọn Stack cần xóa
4. Chọn **Delete**
5. Xác minh xóa stack
6. Đợi vài phút stack chuyển trạng thái sang DELETE_COMPLETE là xóa thành công

![AWS CloudFormation](/images/7.clean/001-clean.png)

#### Xóa S3 bucket

1. Truy cập [giao diện quản trị dịch vụ S3](https://s3.console.aws.amazon.com/s3/home)
  + Click chọn S3 bucket chúng ta đã tạo cho bài thực hành. ( Ví dụ : lab-fcj-bucket-0001 )
  + Click **Empty**.
  + Điền **permanently delete**, sau đó click **Empty** để tiến hành xóa object trong bucket.
  + Click **Exit**.

3. Sau khi xóa hết object trong bucket, click **Delete**

![Clean](/images/7.clean/003-clean.png)

4. Điền tên S3 bucket, sau đó click **Delete bucket** để tiến hành xóa S3 bucket.

![Clean](/images/7.clean/004-clean.png)

#### Xóa EC2 instance

Bước này ta xóa intance đã tạo để có EBS sao lưu

1. Truy cập [giao diện quản trị dịch vụ EC2](https://console.aws.amazon.com/ec2/v2/home)
  + Click **Instances**.
  + Click chọn  instance đã tạo. 
  + Click **Instance state**.
  + Click **Terminate instance**, sau đó click **Terminate** để xác nhận.

![AWS EC2](/images/7.clean/002-cleann.png)
  