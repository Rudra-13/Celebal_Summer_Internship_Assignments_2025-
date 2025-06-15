select   h.hacker_id,h.name,sum(t.max_score) as total_score
from hackers h
join (select
        hacker_id,
        challenge_id,
        max(score) as max_score
    from
        submissions
    group by 
        hacker_id, challenge_id)
        t ON h.hacker_id = t.hacker_id   
 -- t is the temporary table we are making connecting to other tabel colijmns
 group by
        h.hacker_id, h.name
 having
        sum(t.max_score) > 0
order by
        total_score desc,
        h.hacker_id asc;