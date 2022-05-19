--finding last row without using top or bottom
select * from (
select *,ROW_NUMBER()  over(order by Person ) as rn from [dbo].[People]) T 
where T.rn=(
select MAX(r) from(
select *,ROW_NUMBER()  over(order by Person ) as r from [dbo].[People]) t2)


go

select * from (
select *,ROW_NUMBER()  over(order by Person ) as rn from [dbo].[People]) T








