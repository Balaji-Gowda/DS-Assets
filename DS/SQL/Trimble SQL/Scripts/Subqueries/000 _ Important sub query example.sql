
-- 1. Identify top 10 sales per each month
-- 2. Sum each month top 10 sales
-- 3. Compare current month with prev month


select T3.MonthStart
		,T3.SumTotal
		,Ta3.SumTotal

from
(
select MonthStart
	,SumTotal = sum(TotalDue)
from

(
select MonthStart
		,TotalDue
		
from
(
select OrderDate
		,TotalDue
		,MonthStart = DATEFROMPARTS(year(OrderDate),MONTH(OrderDate),1)
		,rank = ROW_NUMBER() over(partition by DATEFROMPARTS(year(OrderDate),MONTH(OrderDate),1) order by TotalDue Desc)
from Sales.SalesOrderHeader
) T1
where T1.rank <=10

) T2
group by MonthStart
)T3

Left join


(
select MonthStart
	,SumTotal = sum(TotalDue)
from

(
select MonthStart
		,TotalDue
		
from
(
select OrderDate
		,TotalDue
		,MonthStart = DATEFROMPARTS(year(OrderDate),MONTH(OrderDate),1)
		,rank = ROW_NUMBER() over(partition by DATEFROMPARTS(year(OrderDate),MONTH(OrderDate),1) order by TotalDue Desc)
from Sales.SalesOrderHeader
) Ta1
where Ta1.rank <=10

) Ta2
group by MonthStart
)Ta3

on T3.MonthStart = DATEADD(month,1,Ta3.MonthStart)
order by 1










































































