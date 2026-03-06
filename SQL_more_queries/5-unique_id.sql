-- Creates the table unique_id with id DEFAULT 1 and UNIQUE constraint
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
