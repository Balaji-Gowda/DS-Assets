create table dbo.Calender
(
Date date,
weekdaynum int,
weekday varchar(20),
startOfMonth date,
year int,
dayNo int,
monthNo int
)
alter table dbo.Calender
add  Weekend tinyint,holiday tinyint
select * from dbo.Calender;

with MyCalender as
(
select cast('01-01-2011' as date) as startdate

union all

select dateadd(day,1,startdate)
from MyCalender
where startdate < CAST('12-31-2030' as date)
)
insert into dbo.Calender
(
Date
)
select * 
from MyCalender
option(maxrecursion 10000)