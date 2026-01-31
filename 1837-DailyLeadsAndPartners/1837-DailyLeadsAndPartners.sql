-- Last updated: 1/31/2026, 2:19:00 PM
# Write your MySQL query statement below
SELECT date_id, make_name, COUNT(DISTINCT(lead_id)) as unique_leads,  COUNT(DISTINCT(partner_id)) as unique_partners
FROM DailySales
GROUP BY date_id,make_name