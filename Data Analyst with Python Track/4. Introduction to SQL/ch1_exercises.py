# Exercise_1 
-- Try running me!
SELECT 'DataCamp <3 SQL'
 AS result;

--------------------------------------------------
# Exercise_2 
#1
SELECT 'SQL'
AS result;
#2
SELECT 'SQL is'
AS result;
#3
SELECT 'SQL is cool!'
AS result;


--------------------------------------------------
# Exercise_3 
#1

SELECT title FROM films
#2
SELECT release_year FROM films

#3
select name
from people;


--------------------------------------------------
# Exercise_4 
#1

SELECT title FROM films
#2
SELECT title, release_year
FROM films;
#3
SELECT title, release_year, country
FROM films;
#4
SELECT *
FROM films;


--------------------------------------------------
# Exercise_5 
#1
SELECT DISTINCT country  FROM films

#2
SELECT DISTINCT certification FROM films

#3
SELECT DISTINCT role FROM roles



--------------------------------------------------
# Exercise_6 
#1
SELECT COUNT(*)
FROM people;
#2
SELECT COUNT(birthdate)
FROM people;
#3
SELECT COUNT(DISTINCT birthdate)
FROM people;
#4
SELECT COUNT(DISTINCT language)
FROM films;
#5
SELECT COUNT(DISTINCT country)
FROM films;


--------------------------------------------------
