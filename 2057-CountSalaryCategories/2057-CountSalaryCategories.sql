-- Last updated: 1/31/2026, 2:18:50 PM
# Write your MySQL query statement below
    SELECT "Low Salary" AS category,COUNT(account_id) AS accounts_count
    FROM Accounts
    Where income < 20000
UNION
    SELECT "High Salary" AS category,COUNT(account_id) AS accounts_count
    FROM Accounts
    Where income > 50000
UNION
    SELECT "Average Salary" AS category,COUNT(account_id) AS accounts_count
    FROM Accounts
    Where income Between 20000 and 50000