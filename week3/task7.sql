-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
-- Enter your query here.
SELECT(COUNT(CITY) - COUNT(DISTINCT CITY)) AS difference FROM STATION;