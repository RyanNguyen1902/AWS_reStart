### DESIGN ARCHITECTURE FOR AI EDUCATION COMPANY
You are a Network Administrator / Cloud Engineer of a company. You recieved an email to inform you that company want you to research about AWS and do a report for both CIO and CTO. 

The current system of your company is running on Microsoft Windows Server. You are searching around on the internet and found this lab that suitable your needs to research and test Windows Server on AWS.

### Design architecture with high availability 


![alt](https://github.com/RyanNguyen1902/AWS_reStart/blob/5b575381d2e783da3ebcb6b4d4d0949da67ede93/AWS_Blog/AI_Education_case/images/AI_EDUCATION%20CASE.drawio.png)

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
