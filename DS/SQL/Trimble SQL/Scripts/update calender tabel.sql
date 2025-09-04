select * from AdventureWorks2019.dbo.Calender;
--update dbo.Calender
--set weekdaynum = 


update AdventureWorks2019.dbo.Calender
set		weekdaynum = DATEPART(WEEKDAY, Date) 
		,weekday = FORMAT(Date,'dddd')
		,startOfMonth = DATEFROMPARTS(year(Date),MONTH(Date),01)
		,year = year(Date)
		,dayNo = day(Date)
		,monthNo = MONTH(Date)
from AdventureWorks2019.dbo.Calender;


update AdventureWorks2019.dbo.Calender
set holiday =
		case 
			when monthNo =1 and dayNo = 1 then 1 
			else 0
		end
