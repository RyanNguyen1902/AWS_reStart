### DESIGN ARCHITECTURE FOR AI EDUCATION COMPANY
You are a Network Administrator / Cloud Engineer of a company. You recieved an email to inform you that company want you to research about AWS and do a report for both CIO and CTO. 

The current system of your company is running on Microsoft Windows Server. You are searching around on the internet and found this lab that suitable your needs to research and test Windows Server on AWS.

### Design architecture with high availability 


![alt](https://github.com/RyanNguyen1902/AWS_reStart/blob/5b575381d2e783da3ebcb6b4d4d0949da67ede93/AWS_Blog/AI_Education_case/images/AI_EDUCATION%20CASE.drawio.png)

Create a custom VPC with multi-AZ in one region to secure web application, we have spread all resources across 2 availability zones to provide for redundancy  

Put Internet gateway into VPC so that resources inside the VPC can communicate with the outside internet

Use route 53 to convert domain to IP addresses

Two web-server are deployed on two EC2 instances ( one instance in 1 public subnet in each AZ ) 

Use elastic load balancer to balance external traffic to the server

The scaling group allow you to add or remove web instances base on demand 

In the database tier, two managed database RDS are deployed in two AZ ( one in each AZ ) to ensure the reliability of database

Master is primary data and slave is backup data 

Put security group in each tier to increase the secure

Use S3 to store data of web-server,  replica of RDS

Application servers in two AZ will get data RDS master

Use Nat gateway so that resources in private subnets can communicate with the internet outside

Use Cloud front connect to S3 and internet gateway to reduce latency and improve performance for global users

Using AWS shield against attack from outside to help minimize application downtime and latency

Cost estimate:
