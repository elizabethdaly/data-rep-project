## MySQL Databases & tables

DB = datarepresentation, table = food

MySQL command to create food table:

create table food (
    id int NOT NULL auto_increment,
    category ENUM('dairy', 'vegetable', 'meat', 'canned'),
    name varchar(250),
    price DECIMAL(6,2) NOT NULL,
    PRIMARY KEY(id)
    );

mysql> desc food;

| Field    | Type                                      | Null | Key | Default | Extra          |
|:---------|:------------------------------------------|:-----|:----|:--------|:---------------|
| id       | int(11)                                   | NO   | PRI | NULL    | auto_increment |
| category | enum('dairy','vegetable','meat','canned') | YES  |     | NULL    |                |
| name     | varchar(250)                              | YES  |     | NULL    |                |
| price    | decimal(6,2)                              | NO   |     | NULL    |                |

## WEB PAGE
1. shopper1.html

## SERVERS

**server_proj1.py**

- basic, no DB or web page

**server_proj2.py**

- basic + DB + webpage
- Price displayed as two decimal places on initial read from DB and after create & update.


## DAO
1. zfoodDAO.py contains foodDAO class

## Final version:
- shopper1.html
- server_proj2.py
- zfoodDAO.py

## References/code help
1. https://stackoverflow.com/questions/30247108/round-all-decimals-from-dynamic-json-to-2-decimal-places
(Accessed 6 Dec 2019)