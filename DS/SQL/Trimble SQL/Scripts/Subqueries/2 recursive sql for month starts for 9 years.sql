with MonthStarts as
(
select cast('01-01-2021' as date) as mon

union all

select DATEAdd(month,1,mon)
from MonthStarts
where mon < CAST('12-01-2029' as date)
)
select * from MonthStarts
option(maxrecursion 110)