-- File: task0
-- Task: Write a SQL script that creates a table users

-- If the table already exists, the script should not fail.
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255) 
);
-- Making the 'email' attribute unique directly in the table schema enforces business rules and avoids application bugs.
