# Exercise_1 
#1
SELECT SUM (duration)
	FROM films;
#2
SELECT AVG (duration)
	FROM films;
#3

	SELECT MIN (duration)
	FROM films;
#4

	SELECT MAX (duration)
	FROM films;


--------------------------------------------------
# Exercise_2 
#1

	SELECT SUM (gross)
	FROM films
#2

	SELECT AVG (gross)
	FROM films
#3

	SELECT MIN (gross)
	FROM films
#4

	SELECT MAX (gross)
	FROM films


--------------------------------------------------
# Exercise_3 
#1

	SELECT SUM(gross)
	FROM films
	WHERE release_year >= 2000;
#2
	SELECT AVG(gross)
	FROM films
	WHERE title LIKE 'A%'
#3
	SELECT MIN(gross)
	FROM films
	WHERE release_year = 1994;
#4
	SELECT MAX(gross)
	FROM films
	WHERE release_year BETWEEN 2000 AND 2012;


--------------------------------------------------
# Exercise_4 
#1
	SELECT title, (gross - budget) AS net_profit
	FROM films;
#2
SELECT title,duration/60.0 AS duration_hours
	FROM films;
#3
	SELECT AVG(duration)  / 60.0 AS avg_duration_hours
	FROM films;


--------------------------------------------------
# Exercise_5 
#1
-- get the count(deathdate) and multiply by 100.0
-- then divide by count(*)

	SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead
	FROM people
#2
	SELECT MAX(release_year) - MIN(release_year) AS difference
	FROM films
#3
	SELECT (MAX(release_year) - MIN(release_year))/10 AS number_of_decades
	FROM films


--------------------------------------------------
