# Exercise_1 
#1
	SELECT name
	FROM people
	ORDER BY name
#2
	SELECT name
	FROM people
	ORDER BY birthdate
#3
	SELECT name,birthdate
	FROM people
	ORDER BY birthdate


--------------------------------------------------
# Exercise_2 
#1
	SELECT title
	FROM films
	WHERE release_year IN (2000, 2012)
	ORDER BY release_year;
#2
	SELECT *
	FROM films
	WHERE release_year <> 2015
	ORDER BY duration;
#3
SELECT title, gross
	FROM films
	WHERE title LIKE 'M%'
	ORDER BY title;


--------------------------------------------------
# Exercise_3 
#1
	SELECT imdb_score, film_id
	FROM reviews
	ORDER BY imdb_score DESC
#2
	SELECT title
	FROM films
	ORDER BY title DESC
#3
	SELECT title, duration
	FROM films
	ORDER BY duration DESC


--------------------------------------------------
# Exercise_4 
#1
	SELECT birthdate, name
	FROM people
	ORDER BY birthdate, name;
#2
	SELECT release_year, duration, title
	FROM films
	ORDER BY release_year, duration;
#3
	SELECT certification, release_year, title
	FROM films
	ORDER BY certification, release_year;
#4
	SELECT name, birthdate
	FROM people
	ORDER BY name, birthdate


--------------------------------------------------
# Exercise_5 
#1

	SELECT release_year, count(*)
	FROM films
	GROUP BY release_year
#2
	SELECT release_year, AVG(duration)
	FROM films
	GROUP BY release_year
#3
	SELECT release_year, MAX(budget)
	FROM films
	GROUP BY release_year
#4
	SELECT imdb_score, COUNT(num_votes)
	FROM reviews
	GROUP BY imdb_score


--------------------------------------------------
# Exercise_6 
#1
	SELECT release_year, MIN(gross)
	FROM films
	GROUP BY release_year
#2
	SELECT language, SUM(gross)
	FROM films
	GROUP BY language
#3
	SELECT country, SUM(budget)
	FROM films
	GROUP BY country
#4
	SELECT release_year, country, MAX(budget)
	FROM films
	GROUP BY release_year, country
	ORDER BY release_year, country
#5
	SELECT country, release_year, MIN(gross)
	FROM films
	GROUP BY release_year, country
	ORDER BY country, release_year


--------------------------------------------------
# Exercise_7 
#1
	SELECT release_year, budget, gross
	FROM films
#2
	SELECT release_year, budget, gross
	FROM films
	WHERE release_year > 1990
#3
	SELECT release_year
	FROM films
	GROUP BY release_year
	HAVING release_year > 1990
#4
	SELECT release_year, AVG(budget) as avg_budget, AVG(gross) as avg_gross
	FROM films
	GROUP BY release_year
	HAVING release_year > 1990
#5
	SELECT release_year, AVG(budget) as avg_budget, AVG(gross) as avg_gross
	FROM films
	GROUP BY release_year
	HAVING AVG(budget) > 60000000
#6
	SELECT release_year, AVG(budget) as avg_budget, AVG(gross) as avg_gross
	FROM films
	GROUP BY release_year
	HAVING AVG(budget) > 60000000
	ORDER BY AVG(gross) DESC;


--------------------------------------------------
# Exercise_8 
-- select country, average budget, average gross
SELECT country, AVG(budget) as avg_budget, AVG(gross) as avg_gross
-- from the films table
FROM films
-- group by country 
GROUP BY country
-- where the country has more than 10 titles
HAVING COUNT(title) > 10
-- order by country
ORDER BY country LIMIT 5
-- limit to only show 5 results

--------------------------------------------------
# Exercise_9 
#1
SELECT title, imdb_score
FROM films
JOIN reviews
ON films.id = reviews.film_id
WHERE title = 'To Kill a Mockingbird';
#2
selected_option = 2


--------------------------------------------------
