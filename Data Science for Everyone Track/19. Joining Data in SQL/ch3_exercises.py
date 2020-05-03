# Exercise_1 
SELECT *
-- 2010 table will be on top
FROM economies2010
-- which set theory clause?
UNION
-- pick specified columns from 2015 table
SELECT *
-- 2015 table on the bottom
FROM economies2015
-- order accordingly
ORDER BY code, year;

--------------------------------------------------
# Exercise_2 
SELECT country_code
FROM cities
UNION
SELECT code as country_code
FROM currencies
ORDER BY country_code

--------------------------------------------------
# Exercise_3 
SELECT code, year
FROM economies
UNION ALL
SELECT country_code, year
FROM populations
ORDER BY code, year;

--------------------------------------------------
# Exercise_4 
SELECT code, year
FROM economies
INTERSECT
SELECT country_code, year
FROM populations
ORDER BY code, year;

--------------------------------------------------
# Exercise_5 
SELECT name
FROM countries
INTERSECT
SELECT name
FROM cities;

--------------------------------------------------
# Exercise_6 
SELECT city.name
FROM cities AS city
EXCEPT
SELECT country.capital
FROM countries AS country
ORDER BY name;

--------------------------------------------------
# Exercise_7 
SELECT country.capital
FROM countries AS country
EXCEPT
SELECT city.name
FROM cities AS city
ORDER BY capital;

--------------------------------------------------
# Exercise_8 
#1
SELECT * FROM countries
WHERE region='Middle East'
#2
SELECT DISTINCT name FROM languages
ORDER BY name

#3
SELECT DISTINCT name FROM languages
WHERE code IN
    (SELECT code FROM countries
    WHERE region='Middle East')
ORDER BY name


--------------------------------------------------
# Exercise_9 
#1

SELECT COUNT(*) FROM countries
WHERE continent = 'Oceania'
#2

SELECT c1.code, c1.name, c2.basic_unit AS currency
FROM countries AS c1
INNER JOIN currencies AS c2
USING (code)
WHERE continent = 'Oceania';
#3
SELECT c1.code, c1.name
FROM countries AS c1
WHERE c1.continent = 'Oceania'
    AND code NOT IN
    (SELECT code 
    FROM currencies);


--------------------------------------------------
# Exercise_10 
SELECT name
-- alias the table where city name resides
FROM cities AS c1
-- choose only records matching the result of multiple set theory clauses
WHERE country_code IN
(
     -- select appropriate field from economies AS e
    SELECT e.code
    FROM economies AS e
    -- get all additional (unique) values of the field from currencies AS c2  
    UNION
    SELECT c2.code
    FROM currencies AS c2
    -- exclude those appearing in populations AS p
    EXCEPT
    SELECT p.country_code
    FROM populations AS p
);

--------------------------------------------------
