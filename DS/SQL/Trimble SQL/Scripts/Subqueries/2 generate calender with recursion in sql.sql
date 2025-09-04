


with DateSeries as(

select CAST('01-01-2021'as date) as MyDate

union all

select DATEADD(day,1,MyDate)
from DateSeries
where MyDate < CAST('12-31-2021' as date)
--where num<100
)

select * from DateSeries
option(maxrecursion 365)