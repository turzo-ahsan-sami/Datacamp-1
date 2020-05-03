# Exercise_1 
#1
-- Select all columns from cities
SELECT *
FROM cities
#2
SELECT * 
FROM cities
  -- 1. Inner join to countries
  INNER JOIN countries
    -- 2. Match on the country codes
    ON cities.country_code = countries.code
#3
-- 1. Select name fields (with alias) and region 
SELECT cities.name AS city, 
        countries.name AS country, 
        countries.region
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code


--------------------------------------------------
# Exercise_2 
-- 3. Select fields with aliases
SELECT c.code AS country_code, 
       c.name, 
       e.year, 
       e.inflation_rate
FROM countries AS c
INNER JOIN economies AS e
ON c.code = e.code;

--------------------------------------------------
# Exercise_3 
#1
-- 4. Select fields
SELECT c.code, c.name, c.region, p.year, p.fertility_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code;
#2
-- 6. Select fields
SELECT c.code, name, region, e.year, fertility_rate, e.unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code;
#3
-- 6. Select fields
SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code AND p.year = e.year;


--------------------------------------------------
# Exercise_4 
SELECT c.name AS country, c.continent, l.name AS language, l.official
FROM countries AS c
INNER JOIN languages AS l
USING(code);

--------------------------------------------------
# Exercise_5 
#1
-- 4. Select fields with aliases
SELECT p1.country_code, 
       p1.size AS size2010,
       p2.size AS size2015
FROM populations AS p1
INNER JOIN populations AS p2
ON  p1.country_code = p2.country_code;
#2
-- 5. Select fields with aliases
SELECT p1.country_code, 
       p1.size AS size2010,
       p2.size AS size2015
FROM populations AS p1
INNER JOIN populations AS p2
ON p1.country_code = p2.country_code
    AND p1.year = p2.year - 5;
#3
SELECT p1.country_code, 
       p1.size AS size2010,
       p2.size AS size2015,
       ((p2.size - p1.size)/p1.size * 100.0) AS growth_perc
FROM populations AS p1
INNER JOIN populations AS p2
ON p1.country_code = p2.country_code
    AND p1.year = p2.year - 5;


--------------------------------------------------
# Exercise_6 
SELECT name, continent, code, surface_area,
    CASE 
        -- first case
        WHEN surface_area > 2000000 THEN 'large'
        -- second case
        WHEN surface_area > 350000 THEN 'medium'
        -- else clause + end
        ELSE 'small' 
    END AS geosize_group
FROM countries;

--------------------------------------------------
# Exercise_7 
#1
SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
FROM populations
WHERE year = 2015;
#2
SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
INTO pop_plus
FROM populations
WHERE year = 2015;

SELECT * FROM pop_plus;
#3
SELECT country_code, size,
    CASE WHEN size > 50000000 THEN 'large'
        WHEN size > 1000000 THEN 'medium'
        ELSE 'small' END
        AS popsize_group
INTO pop_plus
FROM populations
WHERE year = 2015;

SELECT c.name, c.continent, c.geosize_group, p.popsize_group
FROM countries_plus as c
INNER JOIN pop_plus as p
ON c.code = p.country_code
ORDER BY c.geosize_group


--------------------------------------------------
