-- File: create_users_table.sql
-- Task: Create the 'users' table with specified attributes.

-- If the table already exists, the script should not fail.
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);

-- Additional comment: 
-- Making the 'email' attribute unique directly in the table schema enforces business rules and avoids application bugs.
