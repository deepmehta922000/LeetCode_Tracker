-- Last updated: 1/31/2026, 2:18:52 PM
# Write your MySQL query statement below
   select employee_id , 
   case 
        when employee_id%2 <>0 and name not like 'M%' then salary 
        else 0
   end as bonus
   from employees
   order by employee_id;
