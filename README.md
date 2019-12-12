## MySQL Databases & tables

Database = datarepresentation  
Table = food

MySQL command to create food table:
```SQL
create table food (
    id int NOT NULL auto_increment,
    category ENUM('dairy', 'vegetable', 'meat', 'canned'),
    name varchar(250),
    price DECIMAL(6,2) NOT NULL,
    PRIMARY KEY(id)
    );
```
```SQL
desc food;
```

| Field    | Type                                      | Null | Key | Default | Extra          |
|:---------|:------------------------------------------|:-----|:----|:--------|:---------------|
| id       | int(11)                                   | NO   | PRI | NULL    | auto_increment |
| category | enum('dairy','vegetable','meat','canned') | YES  |     | NULL    |                |
| name     | varchar(250)                              | YES  |     | NULL    |                |
| price    | decimal(6,2)                              | NO   |     | NULL    |                |

MySQL commands to add some records to food table:
```SQL
insert into food (category, name, price) values ("meat", "pork", 4.50);
```
```SQL
insert into food (category, name, price) values ("dairy", "milk", 2.99);
```
```SQL
insert into food (category, name, price) values ("canned", "beans", 0.99);
```


## WEB PAGE

**shopper1.html**

- Price displayed as two decimal places on initial read from DB and after create & update.
```javascript
parseFloat(food.Price).toFixed(2)
```

**shopper2.html**

- Try to make web page a bit nicer with CSS Bootstrap: buttons, form

**shopper3.html**

- Try to make layout a bit nicer

## SERVERS

**server_proj1.py**

- basic, no DB or web page

**server_proj2.py**

- basic + DB + webpage
- Allow for decimal type in DB
```python
from decimal import Decimal
```
## DAO
- zfoodDAO.py contains foodDAO class

## Current working version:
- shopper3.html
- server_proj2.py
- zfoodDAO.py

## References/code help
1. https://stackoverflow.com/questions/30247108/round-all-decimals-from-dynamic-json-to-2-decimal-places
(Accessed 6 Dec 2019)
2. https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object/39257479 (Accessed 4 Dec 2019)
3. [Bootstrap](https://getbootstrap.com/docs/3.4/)