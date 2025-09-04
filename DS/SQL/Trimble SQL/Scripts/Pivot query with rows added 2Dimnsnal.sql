

select 
OrderQty,[Accessories],[Bikes],[Clothing],[Components]
from
(select CategoryName = D.Name,
		A.LineTotal,
		A.OrderQty
from Sales.SalesOrderDetail A
join Production.Product B
	on A.ProductID = B.ProductID
join Production.ProductSubcategory C
	on B.ProductSubcategoryID = C.ProductSubcategoryID
join Production.ProductCategory D
	on C.ProductCategoryID = D.ProductCategoryID 
	) T
	
Pivot(
sum(LineTotal)
for CategoryName in ([Bikes],[Clothing],[Accessories],[Components])
) T2

order by OrderQty

