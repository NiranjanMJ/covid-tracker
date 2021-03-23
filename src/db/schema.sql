create database covidtrackerdb;

use covidtrackerdb;

CREATE TABLE Tracker (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
statename VARCHAR(30) NOT NULL,
affected_count VARCHAR(30) NOT NULL,
recoverd_count VARCHAR(50)
);


insert into Tracker values(NULL, 'TamilNadu', 0, 0);
insert into Tracker values(NULL, 'Delhi', 0, 0);
insert into Tracker values(NULL, 'Maharashtra', 0, 0);
insert into Tracker values(NULL, 'Manipur', 0, 0);
insert into Tracker values(NULL, 'Kerala', 0, 0);