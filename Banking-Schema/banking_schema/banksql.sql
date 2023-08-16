/*
Author : Sahil Solanki
Roll   :  11624
 make a database named bank upload this -
use mysql > 
>use bank
>source banksql.sql

*/
create table branch ( bname varchar ( 20 ) ,
bcity varchar ( 20 ) not null ,
assets integer default 0 ,
primary key ( bname )
);
 
create table loan(
lno integer,
amount integer,
bname varchar(20),
primary key ( lno ),
foreign key ( bname ) references branch (bname)
);

create table account(
ano integer,
balance integer,
bname varchar(20),
primary key ( ano ),
foreign key ( bname ) references branch(bname)
 );
 
 
create table employee(
ename varchar(50),
depname varchar(100),
start_date integer,
eid integer,
telno integer,
elength integer,
primary key ( eid )
);



create table payment(
pay_date integer,
pamount integer,
pno integer,
primary key ( pno )
);

create table loan_payment(
lno integer,
pno integer,
primary key(pno),
foreign key ( lno) references loan (lno)
);

create table customer (
cid integer ,
cname varchar(50),
cstreet varchar(100),
ccity varchar (30),
ano integer ,
eid integer,
ctype varchar(20),
primary key ( cid ),
foreign key ( eid ) references employee(eid),
foreign key ( ano ) references account(ano)
 );

 create table borrower (
cid integer ,
lno integer ,
primary key ( lno ,cid),
foreign key ( cid ) references customer(cid) ,
foreign key ( lno ) references loan (lno)
);

create table depositor(
access_date integer,
cid integer,
ano integer,
primary key(cid,ano),
foreign key ( cid ) references customer(cid) ,
foreign key ( ano ) references account (ano)
);
