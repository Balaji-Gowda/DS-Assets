-- dynamic stored proc
create procedure dbo.NameSearch(@NameToSearch varchar(50),@SearchPattern varchar(50))

as

begin
	
	declare @query varchar(max) = 'select * from Person.Person where ' + @NameToSearch + ' like '+'''' + '%' + @SearchPattern + '%' +''''
	exec(@query)
end



-- store proc call
exec  dbo.NameSearch 'FirstName','big'
