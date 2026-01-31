-- Last updated: 1/31/2026, 2:18:58 PM
select user_id,
    count(follower_id) as followers_count
from followers 
group by user_id
order by user_id