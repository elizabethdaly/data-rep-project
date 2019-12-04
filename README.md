## SERVERS
List of servers:
1. server_proj1.py basic, no DB or web page
2. server_proj2.py basic + DB, no webpage

## DAO
1. zfoodDAO.py contains foodDAO class

## SQL Databases & tables
1. datarepresentation with table food

MySQL command to create food table:
create table food (
    id int NOT NULL auto_increment,
    category ENUM('dairy', 'vegetable', 'meat', 'canned'),
    name varchar(250),
    price DECIMAL(6,2) NOT NULL,
    PRIMARY KEY(id)
    );

mysql> desc food;

+----------+-------------------------------------------+------+-----+---------+----------------+
| Field    | Type                                      | Null | Key | Default | Extra          |
+----------+-------------------------------------------+------+-----+---------+----------------+
| id       | int(11)                                   | NO   | PRI | NULL    | auto_increment |
| category | enum('dairy','vegetable','meat','canned') | YES  |     | NULL    |                |
| name     | varchar(250)                              | YES  |     | NULL    |                |
| price    | decimal(6,2)                              | NO   |     | NULL    |                |
+----------+-------------------------------------------+------+-----+---------+----------------+