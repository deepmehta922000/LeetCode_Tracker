-- Last updated: 1/31/2026, 2:18:48 PM
# Write your MySQL query statement below
SELECT 
    employee_id
FROM Employees e
WHERE e.salary < 30000
  AND e.manager_id IS NOT NULL
  AND e.manager_id NOT IN (
        SELECT employee_id FROM Employees
    )
ORDER BY e.employee_id;
