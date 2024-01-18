-- File: Task 3
-- Lists all bands with Glam rock as their main style, ranked by their longevity.

SELECT band_name, DATEDIFF(YEAR, formed, split) AS lifespan
fROM metal_bands
WHERE style like '%Glam rock%'
ORDER BY lifespan desc;

