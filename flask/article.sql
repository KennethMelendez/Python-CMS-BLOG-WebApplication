CREATE DATABASE IF NOT EXISTS articles;

use articles;

CREATE TABLE IF NOT EXISTS `users`(
	`id` int(11) auto_increment primary key,
    `name` varchar(100),
    `email` varchar(100),
    `username` varchar(30),
    `password` varchar(100),
    `register_date` TIMESTAMP DEFAULT current_timestamp
);

CREATE TABLE IF NOT EXISTS `articles`(
	`id` int(11) auto_increment primary key,
	`title` varchar(255), author varchar(100),
	`body` text,
	`create_date` timestamp default current_timestamp
);