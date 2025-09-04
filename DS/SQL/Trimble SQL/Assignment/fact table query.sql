select *
from [dbo].[trainUpdated] t
	left join [dbo].[DIM_Calender] c on c.Date = t.[Updated order date]
	left join [dbo].[DIM_Calender] cal on cal.Date = t.[Updated ship date]
	left join [dbo].[DIM_ShipMode] sm on sm.Ship_mode = t.[Ship Mode]
	left join (
					select distinct
					t.[Customer ID]
					,left(t.[Customer Name], Charindex(' ', replace(t.[Customer Name],'-',' '))-1) as First_Name,
						LTRIM(RIGHT(t.[Customer Name],LEN(t.[Customer Name]) - CHARINDEX(' ', replace(t.[Customer Name],'-',' ')) )) AS Last_Name,
						l.Location_key,
						s.Segment_key,
						l.[Postal Code],
						l.City
	
				from [dbo].[trainUpdated] t
					 left  join [dbo].[DIM_Location] l
						on l.[Postal Code] = t.[Postal Code]  and t.City = l.City and l.[Country] = t.[Country] and t.[State] = l.[State] and l.[Region] = t.[Region]--9789
					left join [dbo].[DIM_Segment] s
						on s.[Segment] = t.Segment  --4824

	) cust 
	on cust.[Customer ID] = t.[Customer ID] and 
	(t.[Customer Name]=concat(cust.first_name,' ',cust.last_name) or t.[Customer Name]=concat(cust.first_name,'-',cust.last_name))  and 
	t.[Postal Code]=cust.[Postal Code] and 
	t.[City]=cust.city
	
	left join Dim_Products p on p.[Product_ID] = t.[Product ID] and p.Product_Name=t."Product Name"  --2261536.78269995
	order by 1


	select *
--sum(t.Sales)
from [dbo].[trainUpdated] t
	left join [dbo].[DIM_Calender] c on c.Date = t.[Updated order date]
	left join [dbo].[DIM_Calender] cal on cal.Date = t.[Updated ship date]
	left join [dbo].[DIM_ShipMode] sm on sm.Ship_mode = t.[Ship Mode]
	left join (select distinct [Customer_Key]
				,[Customer_ID] 
				,[First_Name]
				,[Last_Name]
				,l.[Postal Code]
				,l.city
				from [dbo].[Dim_Customers] c left join dim_location l on c.location_key=l.location_key
	) cust 
	on cust.[Customer_ID] = t.[Customer ID] and 
	(t.[Customer Name]=concat(cust.first_name,' ',cust.last_name) or t.[Customer Name]=concat(cust.first_name,'-',cust.last_name))  and 
	t.[Postal Code]=cust.[Postal Code] and 
	t.[City]=cust.city
	
	left join Dim_Products p on p.[Product_ID] = t.[Product ID] and p.Product_Name=t."Product Name"  --2261536.78269995
	
order by 1

------------------------------------
-- Final fact query

insert into [dbo].[FACT_Sales]
select
	t.[Order ID]
		,c.[Date_key] as [OrderDate_key]
		,cal.[Date_key] as [ShipDate_key]
		,[ShipMode_key] 
		,cust.[Customer_key]
		,[Product_Key]
		,[Sales]
from [dbo].[trainUpdated] t
	left join [dbo].[DIM_Calender] c on c.Date = t.[Updated order date]
	left join [dbo].[DIM_Calender] cal on cal.Date = t.[Updated ship date]
	left join [dbo].[DIM_ShipMode] sm on sm.Ship_mode = t.[Ship Mode]
	left join (select distinct [Customer_Key]
				,[Customer_ID] 
				,[First_Name]
				,[Last_Name]
				,l.[Postal Code]
				,l.city
				from [dbo].[Dim_Customers] c left join dim_location l on c.location_key=l.location_key
	) cust 
	on cust.[Customer_ID] = t.[Customer ID] and 
	(t.[Customer Name]=concat(cust.first_name,' ',cust.last_name) or t.[Customer Name]=concat(cust.first_name,'-',cust.last_name))  and 
	t.[Postal Code]=cust.[Postal Code] and 
	t.[City]=cust.city
	
	left join Dim_Products p on p.[Product_ID] = t.[Product ID] and p.Product_Name=t."Product Name"  --2261536.78269995
	
order by 1


