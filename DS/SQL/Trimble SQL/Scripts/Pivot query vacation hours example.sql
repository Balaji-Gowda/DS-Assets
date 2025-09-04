select * from
(
select JobTitle
		,VacationHours
		,Gender
from HumanResources.Employee 
where JobTitle in ('Sales Representative', 'Buyer', 'Janitor') )T

Pivot(
	avg(VacationHours)
	for JobTitle in ([Sales Representative], [Buyer],[Janitor])
) t2

--output pivot
Gender	Sales Representative	Buyer	Janitor
F			30					54		90
M			31					56		88