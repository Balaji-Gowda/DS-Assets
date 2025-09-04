select 
		Name as SubcategoryName
		,Products = STUFF(
						(
						select '; '+Name  from Production.Product B where A.ProductSubcategoryID = B.ProductSubcategoryID and ListPrice>50
						for xml path('')
						),1,2,'' 
					)
		,ListPrice = STUFF(
						(
						select '; '+CAST(cast(ListPrice as money) as varchar)  from Production.Product B 
						where A.ProductSubcategoryID = B.ProductSubcategoryID
						for xml path('')
						),1,2,'' 
					)
from Production.ProductSubcategory A



