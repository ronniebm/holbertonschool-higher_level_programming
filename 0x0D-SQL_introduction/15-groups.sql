-- Lists number of records with the same score in the second_table.
-- Records in decrementing sort.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;