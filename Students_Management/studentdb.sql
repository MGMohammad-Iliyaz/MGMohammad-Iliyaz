CREATE DATABASE studentdb;
USE studentdb;
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    branch VARCHAR(50)
);
select * from students;
ALTER TABLE students ADD COLUMN roll_no VARCHAR(20);
