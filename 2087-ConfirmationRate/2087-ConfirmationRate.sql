-- Last updated: 1/31/2026, 2:18:49 PM
# Write your MySQL query statement below
select 
    user_id,
    ROUND(
    IFNULL(SUM(action = "confirmed") / Count(c.action),0) ,2
    ) as confirmation_rate
FROM signups s
LEFT JOIN confirmations c
USING(user_id)
GROUP BY s.user_id







