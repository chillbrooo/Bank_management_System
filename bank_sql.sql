create database Bank;
use Bank;
create table personal_details(customerID int primary key,first_name varchar(10),
last_name varchar(10),address varchar(30),
phone_number int not null,aadhaar_number varchar(12)unique,pan_number varchar(10)unique);


create table bank_details(account_number int primary key,customerID int,ifsc_code varchar(6),
account_type varchar(7)check(account_type='current' or account_type='saving'),
foreign key(customerID)references personal_details(customerID));


create table transaction_details(transactionID int primary key,sender_acount int,
reciever_account INT,AMOUNT INT,methon varchar(10));

create table account_details(account_number int,transactionID int,amount int,
closing_balance int,foreign key(transactionID)references transaction_details(transactionID));

select * from personal_details;
select * from  transaction_details;
select * from bank_details;
select * from  account_details;

select * from personal_details;

drop table bank_details;
drop table personal_details;

