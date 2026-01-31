-- Last updated: 1/31/2026, 2:18:38 PM
# Write your MySQL query statement below
select 
    teacher_id,
    (
        COUNT(distinct subject_id)
    ) as cnt
from teacher
group by teacher_id