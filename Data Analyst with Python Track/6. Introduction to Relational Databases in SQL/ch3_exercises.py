# Exercise_1 
#1
-- Count the number of rows in universities
SELECT COUNT(*) FROM universities;
#2
-- Count the number of distinct values in the university_city column
SELECT COUNT(DISTINCT(university_city)) FROM universities;


--------------------------------------------------
# Exercise_2 
-- Try out different combinations
SELECT COUNT(DISTINCT(firstname, lastname)) FROM professors;

--------------------------------------------------
# Exercise_3 
#1
-- Rename the organization column to id
ALTER TABLE organizations
RENAME COLUMN organization TO id;

-- Make id a primary key
ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);
#2
-- Rename the university_shortname column to id
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;

-- Make id a primary key
ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY (id);


--------------------------------------------------
# Exercise_4 
#1
-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

#2
-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);
#3
-- Add the new column to the table
ALTER TABLE professors 
ADD COLUMN id serial;

-- Make id a primary key
ALTER TABLE professors 
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);

-- Have a look at the first 10 rows of professors
SELECT * FROM professors
LIMIT 10;


--------------------------------------------------
# Exercise_5 
#1
-- Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model))
FROM cars;
#2
-- Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model)) 
FROM cars;

-- Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);
#3
-- Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model)) 
FROM cars;

-- Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);

-- Update id with make + model
UPDATE cars
SET id = CONCAT(make, model);
#4
-- Count the number of distinct rows with columns make, model
SELECT COUNT(DISTINCT(make, model)) 
FROM cars;

-- Add the id column
ALTER TABLE cars
ADD COLUMN id varchar(128);

-- Update id with make + model
UPDATE cars
SET id = CONCAT(make, model);

-- Make id a primary key
ALTER TABLE cars
ADD CONSTRAINT id_pk PRIMARY KEY(id);

-- Have a look at the table
SELECT * FROM cars;


--------------------------------------------------
# Exercise_6 
-- Create the table
CREATE TABLE students (
  last_name varchar(128) NOT NULL,
  ssn integer[9] UNIQUE,
  phone_no char(12));

--------------------------------------------------
