-- it creates a table called 'force_name' 
-- on which one variable cannot be NULL.
CREATE TABLE IF NOT EXISTS 
force_name(id INT, name VARCHAR(256) NOT NULL);