select v,
		RANK() over( order by v) as my_rank,
		DENSE_RANK() over( order by v) as den_rank,
		row_number() over( order by v) as row_num

		from [dbo].[dense_rank_demo]
go
select v,RANK() over(partition by v order by v) as rankk,CUME_DIST() over(order by v) as cd ,PERCENT_RANK() over(order by v) as prank,LAG(v,2) over(order by v) as lg,Lead(v) over(order by v) as ld, NTILE(3) over(order by v) as nt,  FIRST_VALUE(v) over( partition by v order by v) from dense_rank_demo
