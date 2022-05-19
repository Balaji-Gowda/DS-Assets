select object_name(object_id),* from sys.columns
where name like 'Date'

go
select count(*) Noofcolumns from SYSCOLUMNS where id=(select id from SYSOBJECTS where name='BitCoin')