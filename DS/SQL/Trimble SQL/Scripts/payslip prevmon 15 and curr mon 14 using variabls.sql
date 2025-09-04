declare @today date =  cast('06-13-2022' as date)
declare @current14 date = datefromparts(year(@today),month(@today),14)
declare @payendDate date = 
	case
		when day(@today) > 15 then datefromparts(year(@today),month(@today),14)
		else dateadd(month,-1,@current14)
	end
declare @paystartDate date = dateadd(day,1,dateadd(month,-1,@payendDate))

select @payendDate
select @paystartDate