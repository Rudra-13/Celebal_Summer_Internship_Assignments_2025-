
-- Enter your query here.
SELECT CITY, LENGTH(CITY) AS LEN FROM STATION
ORDER BY LEN ASC, CITY ASC LIMIT 1;

-- for ascending order  to print 


SELECT CITY, LENGTH(CITY) AS LEN  FROM STATION 
ORDER BY LEN DESC, CITY ASC LIMIT 1;
--  for descending order 