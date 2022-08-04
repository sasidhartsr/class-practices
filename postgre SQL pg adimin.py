HERO
COMPANY
BIKE
ENQUIRY
AND
TEST
RIDE

select *
from ENQUIRY_TEST_RIDE;

create
table
ENQUIRY_TEST_RIDE(Customer_Name
varchar, Mobile_No
int,
Vehicle_Modelm
int, states
varchar, District
varchar,
City
varchar, Existing_Vehicle
int, Dealer_state
varchar,
Dealer_Town
varchar, Dealer
varchar, Brief_About_Enquiry
varchar,
Expected_Date_of_Purchase
int, Gender
varchar, Age
int, Occupation
varchar,
Intended_Usage
varchar);
insert
into
ENQUIRY_TEST_RIDE(Customer_Name, Mobile_No, Vehicle_Modelm,
                  states, District, City, Existing_Vehicle,
                  Dealer_state, Dealer_Town, Dealer, Brief_About_Enquiry,
                  Expected_Date_of_Purchase, Gender, Age, Occupation, intended_Usage)
values('sasidhar', 999999, 2016, 'ap', 'chittoor',
       'tirupati', 2018, 'Andhar pradhesh',
       'ctr', 'tsr', 'nooo', 12080239, 'male', 34,
       'salary', 'full_usage');
insert
into
ENQUIRY_TEST_RIDE(Customer_Name, Mobile_No, Vehicle_Modelm, states,
                  District, City, Existing_Vehicle, Dealer_state,
                  Dealer_Town, Dealer, Brief_About_Enquiry,
                  Expected_Date_of_Purchase, Gender, Age,
                  Occupation, intended_Usage)
values('gowthami', 8888, 2015, 'kr', 'karanataka', 'tirupati',
       2014, 'telangana', 'ctr', 'ysr', 'no', 98765,
       'fmale', 38, 'salary', 'full_usage'),
('tsr', 7777, 2014, 'up', 'telangana', 'dhilli', 2012,
 'up', 'ctr', 'kcr', 'no', 53434323, 'male', 39, 'business',
 'mediuam_usage');
select *
from ENQUIRY_TEST_RIDE where

age = 39
update
ENQUIRY_TEST_RIDE
set
age = 23
where
customer_name = 'gowthami';
select *
from ENQUIRY_TEST_RIDE

select *
from ENQUIRY_TEST_RIDE where

age > 25;

KXN
EMPLOYEES

select *
from kxn_employees;

create
table
kxn_employees(name
varchar, age
int, gender
varchar, mobile
int, salary
int, pf_no
int, address
varchar);
insert
into
kxn_employees(name, age, gender, mobile, salary, pf_no, address)
values('ysr', 99, 'male', 134134, 9000, 343, 'ctr');
insert
into
kxn_employees(name, age, gender, mobile, salary, pf_no, address)
values('kcr', 78, 'male', 454545, 9001, 333, 'ctr'), ('ktr', 55, 'male', 67676, 7878, 898, 'tpt');
select *
from kxn where

mobile = 134134;
update
kxn_employees
set
mobile = 70975353
where
name = 'ysr';

update
kxn_employees
set
mobile = 70975353
where
name = 'kcr';
select *
from kxn_employees;

select *
from kxn_employees where

age > 60;

DELETE
FROM
public.kxn_employees
WHERE
name = 'ysr';

TSR_
COLLEGE
details

create
table
tsr_colleage(Name_std
varchar, Age_std
int, salary
int, city
varchar)
select *
from tsr_colleage

insert
into
tsr_colleage(Name_std, Age_std, salary, city)
values('sasi', 18, 2000, 'ctr')
select *
from tsr_colleage

insert
into
tsr_colleage(Name_std, Age_std, salary, city)
values('gowthami', 15, 6000, 'tpt'), ('ysr', 19, 7000, 'blr'), ('kcr', 23, 8000, 'ctr'),
('ktr', 23, 9000, 'tpt'), ('tsr', 14, 8000, 'ctr'), ('sss', 15, 9000, 'ctr'), ('ggg', 17, 9000, 'tpt'),
('ttt', 19, 7000, 'blr'), ('reddy', 17, 8000, 'blr'), ('www', 20, 7000, 'tpt')

update
tsr_colleage
set
age_std = 15
where
name_std = 'gowthami'
select *
from tsr_colleage

select *
from tsr_colleage where

age_std < 18
select *
from tsr_colleage where

age_std > 18

select *
from tsr_colleage where

salary = 9000
select *
from tsr_colleage where

salary >= 9000
select *
from tsr_colleage where

city = 'ctr'
select *
from tsr_colleage where

city = 'blr'