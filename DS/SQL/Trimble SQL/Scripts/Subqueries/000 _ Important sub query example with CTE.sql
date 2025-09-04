with 
sales as
(
	select OrderDate
		,TotalDue
		,MonthStart = DATEFROMPARTS(year(OrderDate),MONTH(OrderDate),1)
		,rank = ROW_NUMBER() over(partition by DATEFROMPARTS(year(OrderDate),MONTH(OrderDate),1) order by TotalDue Desc)
	from Sales.SalesOrderHeader
),
Top10SalSum as
(
select MonthStart
	,SumTotal = sum(TotalDue) 
			
	from
	sales
	
	where rank <=10
	 group by MonthStart
)
select A.MonthStart,A.SumTotal,B.SumTotal as PrevMonthSalTotal
from Top10SalSum A
left join Top10SalSum B
on A.MonthStart = DATEADD(month,1,B.MonthStart)
order by 1
