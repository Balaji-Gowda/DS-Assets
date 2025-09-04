select 
[Mountain Bikes],
[Jerseys],
[Socks],
[Caps],
[Helmets],
[Road Bikes],
[Mountain Frames]
from

(
select SubCategoryName = C.Name,
		A.LineTotal
from Sales.SalesOrderDetail A
join Production.Product B
	on A.ProductID = B.ProductID
join Production.ProductSubcategory C
	on B.ProductSubcategoryID = C.ProductSubcategoryID
where C.Name in ('Mountain Bikes',
'Jerseys',
'Socks',
'Caps',
'Helmets',
'Road Bikes',
'Mountain Frames')
) T1

Pivot(
	stdev(LineTotal)
	for SubCategoryName in ([Mountain Bikes],
[Jerseys],
[Socks],
[Caps],
[Helmets],
[Road Bikes],
[Mountain Frames]
)
) T2


