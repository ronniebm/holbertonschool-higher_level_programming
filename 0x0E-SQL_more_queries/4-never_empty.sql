-- it creates a table 'id_not_null' where 
-- id has default value = 1.
CREATE TABLE IF NOT EXISTS 
id_not_null(id INT DEFAULT 1, name VARCHAR(256));