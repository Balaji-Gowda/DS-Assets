select Category, MAX(sale) from (
select Category,[Customer Name],SUM(Sales) as sale from [dbo].[Orders$] group by [Customer Name],Category) as T group by Category