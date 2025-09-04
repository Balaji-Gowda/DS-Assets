select SalesOrderID
		,OrderDate
		,SubTotal
		,TaxAmt
		,Freight
		,TotalDue
		,[Line Totals] = 

				STUFF(
				(
				select ','+cast(cast(LineTotal as money) as varchar) from Sales.SalesOrderDetail B where A.SalesOrderID = B.SalesOrderID
				for xml path('')
				)
				,1,1,'')

from Sales.SalesOrderHeader A


