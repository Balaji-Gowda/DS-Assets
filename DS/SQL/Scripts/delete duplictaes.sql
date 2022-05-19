WITH CTE([colA], 
    [colB],
    DuplicateCount)
AS (SELECT [colA], 
           [colB], 
           ROW_NUMBER() OVER(PARTITION BY [colA], 
                                          [colB]
           ORDER BY colA) AS DuplicateCount
    FROM [dbo].[sample])
DELETE FROM CTE
WHERE DuplicateCount > 1;