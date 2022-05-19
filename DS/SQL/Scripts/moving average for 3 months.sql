--select [Order Date] from  Orders1 order by [Order date]
--go
select [Order date] from  Orders1 where [Order Date] >
(select	
DATEADD(M,-3,Max([Order Date])) from Orders1) order by [Order Date] desc
go
select [Order Date] from Orders1 order by [Order Date] desc

--max date
select 
max([Order Date]) from Orders1
--3 months back from max date
select	DATEADD(M,-3,Max([Order Date])) from Orders1
--order date ordered desc
select [Order Date] from Orders1 order by [Order Date] desc


--moving average for 3 months
select [Order Date],AVG(Total_Sale) over (Order by [Order Date]  rows between 4 preceding and current row) as [Moving average Sql]
from sales_gb_OD where [Order Date] <(select	
DATEADD(M,3,Min([Order Date])) from Orders1)