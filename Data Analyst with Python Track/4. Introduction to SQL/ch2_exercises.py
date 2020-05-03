# Exercise_1 
#1
SELECT *
FROM films
WHERE release_year = 2016;
#2
SELECT COUNT(*)
	FROM films
	WHERE release_year < 2000;
#3
SELECT *
	FROM films
	WHERE release_year > 2000;


--------------------------------------------------
# Exercise_2 
#1

	SELECT *
	FROM films
	WHERE language = 'French';
#2

	SELECT *
	FROM people
	WHERE birthdate = '1974-11-11';
#3

	SELECT COUNT(language)
	FROM films
	WHERE language = 'Hindi';
#4

	SELECT *
	FROM films
	WHERE certification = 'R';


--------------------------------------------------
# Exercise_3 
#1

	SELECT title, release_year
	FROM films
	WHERE language = 'Spanish' and release_year < 2000
#2

	SELECT *
	FROM films
	WHERE language = 'Spanish' and release_year > 2000
#3

	SELECT *
	FROM films
	WHERE language = 'Spanish' and release_year > 2000 and release_year < 2010


--------------------------------------------------
# Exercise_4 
#1

	SELECT title, release_year
	FROM films
	WHERE release_year >= 1990 AND release_year <2000
#2

	SELECT title, release_year
	FROM films
	WHERE (release_year >= 1990 AND release_year <2000)
	AND (language = 'French' OR language = 'Spanish');
#3

	SELECT title, release_year
	FROM films
	WHERE (release_year >= 1990 AND release_year <2000)
	AND (language = 'French' OR language = 'Spanish')
	AND gross > 2000000;


--------------------------------------------------
# Exercise_5 
#1

	SELECT title, release_year
	FROM films
	WHERE release_year BETWEEN 1990 AND 2000;
#2

	SELECT title, release_year
	FROM films
	WHERE release_year BETWEEN 1990 AND 2000
	AND budget > 100000000;
#3

	SELECT title, release_year
	FROM films
	WHERE release_year BETWEEN 1990 AND 2000
	AND budget > 100000000
	AND language = 'Spanish';
#4

	SELECT title, release_year
	FROM films
	WHERE release_year BETWEEN 1990 AND 2000
	AND budget > 100000000
	AND (language = 'Spanish' OR language = 'French');


--------------------------------------------------
# Exercise_6 
#1
	SELECT title, release_year
	FROM films
	WHERE release_year IN(1990, 2000)
	AND duration > 120;
#2

	SELECT title, language
	FROM films
	WHERE language IN('English', 'Spanish', 'French');
#3

	SELECT title, certification
	FROM films
	WHERE certification IN('NC-17', 'R');


--------------------------------------------------
# Exercise_7 
#1

	SELECT name, deathdate
	FROM people
	WHERE deathdate IS null;
#2
	SELECT title
	FROM films
	WHERE budget IS null;
#3
	SELECT COUNT(*)
	FROM films
	WHERE language IS NULL;


--------------------------------------------------
# Exercise_8 
#1
	SELECT name
	FROM people
	WHERE name LIKE 'B%'
#2
	SELECT name
	FROM people
	WHERE name LIKE '_r%'
#3
	SELECT name
	FROM people
	WHERE name NOT LIKE 'A%'


--------------------------------------------------
