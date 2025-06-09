-- vowels name finding question
select distinct city 
from STATION
where lower(substr(city,1,1)) in ('a','e','i','o','u')
and lower(substr(city,-1,1)) in ('a','e','i','o','u'); 