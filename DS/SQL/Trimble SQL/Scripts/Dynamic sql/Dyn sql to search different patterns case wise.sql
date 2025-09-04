-- dynamic stored proc
create procedure dbo.NameSearchWithType(@NameToSearch varchar(50),@SearchPattern varchar(50),@MatchType int)

as

begin

	if @MatchType = 1
		begin
			declare @query varchar(max) = 'select * from Person.Person where ' + @NameToSearch +' = ' + ''''+@SearchPattern + ''''
			exec(@query)
		end

	if @MatchType = 2
	begin
		declare @query2 varchar(max) = 'select * from Person.Person where ' + @NameToSearch + ' like '+'''' + @SearchPattern + '%' +''''
		exec(@query2)
	end

	if @MatchType = 3
		begin
			declare @query3 varchar(max) = 'select * from Person.Person where ' + @NameToSearch + ' like '+'''' + '%' + @SearchPattern +''''
			exec(@query3)
		end

	if @MatchType = 4
	begin
		declare @query4 varchar(max) = 'select * from Person.Person where ' + @NameToSearch + ' like '+'''' + '%' + @SearchPattern + '%' +''''
		exec(@query4)
	end

end



-- store proc call
exec  dbo.NameSearchWithType 'FirstName','jason', 1


