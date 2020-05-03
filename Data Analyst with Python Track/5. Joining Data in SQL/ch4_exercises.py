# Exercise_1 
#1

SELECT AVG(life_expectancy)
FROM populations
WHERE year = 2015;
#2
SELECT *
FROM populations
WHERE life_expectancy > 1.15 *
    (SELECT AVG(life_expectancy)
    FROM populations
    WHERE year = 2015)
    AND year = 2015;


--------------------------------------------------
# Exercise_2 
SELECT city.name, city.country_code, city.urbanarea_pop
-- from the cities table
FROM cities AS city
-- with city name in the field of capital cities
WHERE city.name IN
  (SELECT capital
   FROM countries)
ORDER BY urbanarea_pop DESC;

--------------------------------------------------
# Exercise_3 
#1
SELECT countries.name AS country, COUNT(*) AS cities_num
FROM cities
INNER JOIN countries
ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;
#2
SELECT countries.name AS country,
  (SELECT COUNT(*)
   FROM cities
   WHERE countries.code = cities.country_code) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;


--------------------------------------------------
# Exercise_4 
#1

SELECT code, COUNT(name) AS lang_num
FROM languages
GROUP BY code;
#2

SELECT local_name, subquery.lang_num
FROM countries, 
    (SELECT code, COUNT(name) AS lang_num
    FROM languages
    GROUP BY code) as subquery
WHERE countries.code = subquery.code
ORDER BY lang_num DESC;


--------------------------------------------------
# Exercise_5 
#1

SELECT name, continent, inflation_rate
FROM countries 
INNER JOIN economies
USING (code)
WHERE year = 2015;
#2

SELECT MAX(inflation_rate) AS max_inf
  FROM (
      SELECT name, continent, inflation_rate
      FROM countries
      INNER JOIN economies
      USING (code)
      WHERE year = 2015) AS subquery
GROUP BY continent;
#3
SELECT name, continent, inflation_rate
FROM countries
INNER JOIN economies
ON countries.code = economies.code
WHERE year = 2015
    AND inflation_rate IN (
        SELECT MAX(inflation_rate) AS max_inf
        FROM (
             SELECT name, continent, inflation_rate
             FROM countries
             INNER JOIN economies
             ON countries.code = economies.code
             WHERE year = 2015) AS subquery
        GROUP BY continent);


--------------------------------------------------
# Exercise_6 
SELECT code, inflation_rate, unemployment_rate
FROM economies
WHERE year = 2015 AND code NOT IN
  (SELECT code
   FROM countries
   WHERE (gov_form = 'Constitutional Monarchy' OR gov_form LIKE '%Republic'))
ORDER BY inflation_rate;

--------------------------------------------------
# Exercise_7 
SELECT DISTINCT c.name, e.total_investment, e.imports
FROM countries AS c
LEFT JOIN economies AS e
ON (c.code = e.code AND c.code IN 
    (SELECT code 
    FROM languages
    WHERE official = 'true'))
WHERE year = 2015 AND region = 'Central America'
ORDER BY c.name;

--------------------------------------------------
# Exercise_8 
SELECT region, continent, AVG(fertility_rate) AS avg_fert_rate
-- left table
FROM countries AS c
-- right table
INNER JOIN populations AS p
-- join conditions
ON c.code = p.country_code
-- specific records matching a condition
WHERE year = 2015
-- aggregated for each what?
GROUP BY region, continent
-- how should we sort?
ORDER BY avg_fert_rate;

--------------------------------------------------
# Exercise_9 
SELECT name, country_code, city_proper_pop, metroarea_pop,  
      city_proper_pop / metroarea_pop * 100 AS city_perc
FROM cities
WHERE name IN
  (SELECT capital
   FROM countries
   WHERE (continent = 'Europe'
      OR continent LIKE '%America'))
     AND metroarea_pop IS NOT NULL
ORDER BY city_perc DESC
LIMIT 10;

--------------------------------------------------
