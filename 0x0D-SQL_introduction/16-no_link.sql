-- Script lists all records of table unless there's no name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;