-- all records of the table with  a feew conditions

SELECT score, name FROM second_table
WHERE name != ""
ORDER BY score DESC;
