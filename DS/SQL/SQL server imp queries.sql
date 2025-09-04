--Query to populate column names

DECLARE @SchemaName NVARCHAR(128) = 'dw';
DECLARE @TableName NVARCHAR(128) = 'PhaseDim';
DECLARE @Columns NVARCHAR(MAX) = '';

SELECT @Columns = @Columns + '[' + COLUMN_NAME + '], '
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = @SchemaName AND TABLE_NAME = @TableName
ORDER BY ORDINAL_POSITION;

SET @Columns = LEFT(@Columns, LEN(@Columns) - 1); -- Remove trailing comma

SELECT @Columns AS ColumnNames;

--query to find tables in which desired columns are present

SELECT 
DB_NAME() AS database_name,
    SCHEMA_NAME(t.schema_id) AS schema_name,
    c.name AS column_name,
    t.name AS table_name
FROM 
    sys.columns c
INNER JOIN 
    sys.tables t ON c.object_id = t.object_id
WHERE 
    c.name = 'Your_col_name'
	
select
        costCenterID = cc.id
        ,companyCode = cc.Company_Code
        ,companyID = comp.id
        ,costCenterCode = cc.Cost_Center_Code
        ,description = cc.Cost_Center_Description
        ,costGroupList = cast(isnull(stuff((select ', ' + cast(rtrim(cg_list.Cost_Group_Code) as varchar(max))
											from stage.EM_COST_GROUP_LIST_MC cg_list
											where cg_list.Company_Code = cc.Company_Code
											and cg_list.Cost_Center_Code = cc.Cost_Center_Code
											for xml path('')
											), 1, 2, ''),'') as varchar(250))

    from stage.EM_COST_CENTERS_MC cc

    inner join stage.PA_COMPANY_INFORMATION comp
    on comp.Company_Code = cc.Company_Code
