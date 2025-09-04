declare  @cols as varchar(max) = STUFF((
					select top 3
						 ' ,['+p.[Product_ID]+']'
					from  [dbo].[FACT_Sales] fs
						left join [dbo].[DIM_Products] p
							on p.[Product_Key] = fs.[Product_key]
					group by p.[Product_ID]
					order by sum(Sales) desc
            FOR XML PATH('')
			, TYPE
            ).value('.', 'NVARCHAR(MAX)') 
        ,1,2,'')
declare @query as varchar(max);

set @query= 'select * from 	
	(
		select 
			p.Product_ID
			,l.Region
			,fs.Sales
		from  [dbo].[FACT_Sales] fs
			join [dbo].[DIM_Products] p
				on p.[Product_Key] = fs.[Product_key]
			left join [dbo].[Dim_Customers] c
				on c.[Customer_Key] = fs.[Customer_key]
			left join [dbo].[DIM_Location] l
				on l.Location_key = c.Location_key
		where p.[Product_ID] in 
					(
					select top 3
						p.[Product_ID]
					from  [dbo].[FACT_Sales] fs
						left join [dbo].[DIM_Products] p
							on p.[Product_Key] = fs.[Product_key]
					group by p.[Product_ID]
					order by sum(Sales) desc
					)
	) T
Pivot
(
	sum(Sales)
	for Product_ID in ('+@cols+'
				--[TEC-CO-10004722],
				--[OFF-BI-10003527],
				--[TEC-MA-10002412]
			)
) t2'

exec(@query)


