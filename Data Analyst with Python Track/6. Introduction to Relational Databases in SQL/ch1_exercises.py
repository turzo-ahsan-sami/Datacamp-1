# Exercise_1 
#1
-- Query the right table in information_schema
SELECT table_name 
FROM information_schema.tables
-- Specify the correct table_schema value
WHERE table_schema = 'public';
#2
-- Query the right table in information_schema to get columns
SELECT column_name, data_type 
FROM information_schema.columns  
WHERE table_name = 'university_professors' AND table_schema = 'public';
#3
selected_option = 3
#4
-- Query the first five rows of our table
SELECT * 
FROM university_professors 
LIMIT 5;


--------------------------------------------------
# Exercise_2 
#1
-- Create a table for the professors entity type
CREATE TABLE professors  (
 firstname  text,
 lastname text
);

-- Print the contents of this table
SELECT * 
FROM professors
#2
-- Create a table for the universities entity type
CREATE TABLE universities (
 university_shortname text,
 university text,
 university_city text);


-- Print the contents of this table
SELECT * 
FROM universities


--------------------------------------------------
# Exercise_3 
-- Add the university_shortname column
ALTER TABLE professors
ADD COLUMN university_shortname text;
-- Print the contents of this table
SELECT * 
FROM professors

--------------------------------------------------
# Exercise_4 
#1
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;
#2
-- Rename the organisation column
ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

-- Delete the university_shortname column
ALTER TABLE affiliations
DROP COLUMN university_shortname;


--------------------------------------------------
# Exercise_5 
#1
-- Insert unique professors into the new table
INSERT INTO professors 
SELECT DISTINCT firstname, lastname, university_shortname 
FROM university_professors;

-- Doublecheck the contents of professors
SELECT * 
FROM professors;
#2
-- Insert unique affiliations into the new table
INSERT INTO affiliations 
SELECT DISTINCT firstname, lastname, function, organization 
FROM university_professors;

-- Doublecheck the contents of affiliations
SELECT * 
FROM affiliations;


--------------------------------------------------
# Exercise_6 
-- Delete the university_professors table
DROP TABLE university_professors;

--------------------------------------------------
