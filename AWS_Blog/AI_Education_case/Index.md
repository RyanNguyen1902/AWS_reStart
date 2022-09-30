### DESIGN ARCHITECTURE FOR AI EDUCATION COMPANY
You are a Network Administrator / Cloud Engineer of a company. You recieved an email to inform you that company want you to research about AWS and do a report for Customer. 

### Design architecture with high availability 


![alt](https://github.com/RyanNguyen1902/AWS_reStart/blob/24d24eda2f3ea85396c8aa6e25585987061790b9/AWS_Blog/AI_Education_case/images/AI_EDUCATION%20CASE.drawio%20(1).png)

Create a custom VPC with multi-AZ in one region to secure Application, we have spread all resources across 2 availability zones to provide for redundancy. 

Use VPN site to site and virtual gateway for migration from On-premese to Cloud

Put Internet gateway into VPC so that resources inside the VPC can communicate with the outside internet

Two App are deployed on two EC2 instances( each instance in 1 public subnet in each AZ ) 

In the database tier, two managed database RDS are deployed in two AZ ( one in each AZ ) to ensure the reliability of database

Master is primary data and slave is backup data 

Application servers in two AZ will get data RDS master

Use Application load balance and Auto scaling group allow you to add or remove instances base on demand 

Use Cloudwatch, Identity and Access, and AWS console Management (IAM) for monitoring and administration.

Use Simple Storage Service for storage

Use Simple Notification Service to notify email or SMS user or administrator

Cost estimate: 

![alt](https://github.com/RyanNguyen1902/AWS_reStart/blob/1dc41bf5621e19338759ce534ddb24c1f26e6895/AWS_Blog/AI_Education_case/images/Estimate.PNG)

Detail:
https://calculator.aws/#/estimate?id=9f482b792d8f8828814495feaeceece6425f17f1
https://github.com/RyanNguyen1902/AWS_reStart/blob/main/AWS_Blog/AI_Education_case/Introduction/AWS%20Pricing%20Calculator.pdf
