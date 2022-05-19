--create table defaultColTab(name varchar(10), DOJ date default '2020-01-20')
select * from defaultColTab

insert into defaultColTab(name,DOJ) values('Teddy',convert(date, '17-12-15',3))