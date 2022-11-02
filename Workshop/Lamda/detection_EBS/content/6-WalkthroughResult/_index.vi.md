+++
title = "Kết quả"
date = 2021
weight = 6
chapter = false
pre = "<b>6. </b>"
+++

#### Kiểm tra giải pháp haotj động.

Chúng ta cùng xem giải pháp hoạt động

#### AWS Backup

1. Để xem giải pháp đang hoạt động, bạn sẽ cần tạo một số bản sao lưu cho Amazon EBS volume. Nếu bạn không ngại chờ đợi, gói AWS Backup sẽ bắt đầu các bản sao lưu hàng ngày đầu tiên vào ngày mai. Nhưng nếu bạn muốn xem quy trình hoạt động ngay bây giờ, bạn có thể điều hướng đến trang tổng quan AWS Backup và trong phần **On-demand backup** Sao lưu theo yêu cầu,
   + Select the **Create on-demand backup** button.

![Backup-Dashboard](/images/6.WalkthroughResult/001-Backup-Dashboard.png?featherlight=false&width=90pc)


2. Lúc này, bạn sẽ thấy một màn hình cho phép bạn tạo một bản sao lưu.

![Backup-On-Demand](/images/6.WalkthroughResult/002-Backup-On-Demand.png?featherlight=false&width=90pc)

  Đối với **Resource type**, hãy chọn EBS. Đối với **Volume ID**, hãy chọn một ổ đĩa EBS hiện có để sao lưu. Với mục đích của hướng dẫn này, việc chọn EBS volume nhỏ hơn sẽ dẫn đến thời gian sao lưu nhanh hơn. Nếu bạn không có một tập EBS hiện có, thì cách đơn giản nhất để tạo khởi chạy phiên bản Amazon Elastic Compute Cloud (Amazon EC2). Khi phiên bản được khởi chạy, Volume ID của nó sẽ hiển thị trong danh sách sau khi màn hình được làm mới.

  Sau khi chọn hai mục này, hãy nhấp vào nút **Create on-demand backup** ở cuối màn hình để bắt đầu sao lưu. Quá trình sao lưu sẽ bắt đầu và bạn sẽ được thông báo về trạng thái của nó. Ban đầu, bản sao lưu sẽ được liệt kê là  **Created** và sau đó cuối cùng sẽ chuyển sang **Completed**. . Khi ở trạng thái Đã hoàn thành **Completed**, AWS Backup sẽ xuất bản một sự kiện lên Amazon EventBridge và đường dẫn sẽ tắt và đang chạy!

  ![Backup-EBS](/images/6.WalkthroughResult/007-Backup-ebs.PNG?featherlight=false&width=90pc)

#### Amazon CloudWatch

3. Bây giờ chúng ta bắt đầu xem tiến trình sao lưu đầu, xem **Amazon CloudWatch** để xem điều gì đang xảy ra. Điều hướng đến trang tổng quan Amazon CloudWatch và chọn liên kết **All alarms** trong ngăn điều hướng bên trái. Có thể mất một khoảng thời gian để sự kiện AWS Backup đi qua toàn bộ quá trình, nhưng bạn sẽ sớm thấy một cảnh báo mới có tên tương tự như những gì được hiển thị ở đây.

![CloudWatch-Dashboard](/images/6.WalkthroughResult/003-CloudWatch-Dashboard.png?featherlight=false&width=90pc)

Cảnh báo được tạo bởi chức năng AWS Lambda mà chúng ta đã triển khai và nó được định cấu hình để phát hiện các điểm bất thường dựa trên chỉ số tùy chỉnh Amazon CloudWatch sẽ được gửi trong các lần sao lưu tiếp theo.

4. Nếu bạn nhấp vào liên kết cảnh báo mới tạo, bạn sẽ được đưa đến màn hình hiển thị thông tin chi tiết của cảnh báo.

![CloudWatch-Alarm-Empty](/images/6.WalkthroughResult/004-CloudWatch-Alarm-Empty.png?featherlight=false&width=90pc)

Tại thời điểm này, chúng ta không có bất kỳ dữ liệu chỉ số nào, vì vậy, cảnh báo hiển thị **insufficient data**. Trên thực tế, để mô hình phát hiện bất thường của Amazon CloudWatch được triển khai, chúng ta sẽ cần trải qua một số lần lặp lại sao lưu trước khi có thể thiết lập một mẫu.

5. Tiếp tục thực hiện các bản sao lưu bổ sung đó, đây là những gì bạn có thể mong đợi thấy sau khi mô hình đã được triển khai đầy đủ.

![CloudWatch-Alarm-Populated](/images/6.WalkthroughResult/005-CloudWatch-Alarm-Populated.png?featherlight=false&width=90pc)

Kiểm tra ngay bây giờ, một số lượng đáng kể các bản sao lưu đã được thực hiện và bạn sẽ nhận thấy một dải màu xám trải dài trên màn hình. Đây là dải phát hiện bất thường và khi các ảnh chụp nhanh snapshots = hiện tại và trước đó được so sánh và có quá nhiều blocks thay đổi, ngưỡng dải xám sẽ bị phá vỡ và cảnh báo được kích hoạt.

6. Cuối cùng, hãy xem chỉ số tùy chỉnh Amazon CloudWatch thực tế. Nếu bạn nhấp vào nút **View in metrics** ở phần trên bên phải của biểu đồ, bạn sẽ được chuyển hướng đến trang số liệu, nơi bạn có thể xem tất cả các điểm dữ liệu chỉ số và cả chỉ số và phát hiện sự bất thường của nó cấu hình.

![CloudWatch-Alarm-Populated](/images/6.WalkthroughResult/006-CloudWatch-Metrics.png?featherlight=false&width=90pc)

#### Kết luận

Phát hiện những điểm bất thường trong dữ liệu của bạn là một cách quan trọng để vượt qua các cuộc tấn công mạng và ransomware. Trong bài Lab này, chúng ta đã xây dựng một serverless anomaly-detection pipeline bằng cách sử dụng các dịch vụ gốc trong AWS để xác định các điểm bất thường trong Amazon EBS Volumes trong quá trình sao lưu. Bằng cách sử dụng khả năng máy học tích hợp mạnh mẽ của Amazon CloudWatch, hoạt động bất thường sẽ xuất hiện và bạn được cảnh báo khi kích thước sao lưu ảnh chụp nhanh vi phạm một dải ngưỡng. Điều này cho phép bạn theo dõi liên tục dữ liệu quan trọng của mình.