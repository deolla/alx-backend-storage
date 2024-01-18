-- File: Task 2
-- Task: Rank country orgins of band ordered by number of (non-unique) fans

-- Create a temporary table to store the rankings
CREATE TEMPORARY TABLE temp_rankings AS (
    SELECT origin, COUNT(*) AS nb_fans
    FROM metal_bands
    GROUP BY origin
);

-- Rank the countries based on the number of fans in descending order
SET @rank = 0;
SELECT origin, nb_fans, @rank := @rank + 1 AS rank
FROM temp_rankings
ORDER BY nb_fans DESC;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS temp_rankings;
