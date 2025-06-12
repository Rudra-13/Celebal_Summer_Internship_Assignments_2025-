select wands.id, wands_property.age, wands.coins_needed, wands.power
from wands 
join wands_property on wands.code=wands_property.code
where wands_property.is_evil = 0
and wands.coins_needed = (
select min(w1.coins_needed)          
from wands w1
join  wands_property wp1 on w1.code = wp1.code
where wp1.is_evil = 0
      and w1.power = wands.power
      and wp1.age =wands_property.age )
order by 
wands.power desc,wands_property.age desc;