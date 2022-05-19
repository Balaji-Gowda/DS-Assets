select * from [dbo].[employees]
go

--employees with max salary from each dept and their names
select e1.FIRST_NAME, e1.JOB_ID, e1.SALARY from (select max(SALARY) as sal, JOB_ID from [dbo].[employees] group by JOB_ID) as e2
inner join [dbo].[employees] e1
on e1.JOB_ID=e2.JOB_ID
and e1.SALARY=e2.sal

go
select JOB_ID,COUNT(*) from [dbo].[employees] group by JOB_ID