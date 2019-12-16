## 1. Hosting the application on eu.pythonanywhere.com (PA)

GiHub repository (public): https://github.com/elizabethdaly/deploytoPA
- server: application.py
- web page: shopper5.html
- DAO: zfood.py
- DB config to edit on PA: dbconfigtemplate.py
- Virtual environment requirements: requirements.txt
- Very basic index: index.html

- All old files in \oldservers

- Link to app on pythonanywhere: http://elizabethdaly.eu.pythonanywhere.com/shopper5.html

It even looks ok on my phone.

## 2. Hosting the application on my local machine

This project is hosted on GitHub at https://github.com/elizabethdaly/data-rep-project
- server: server_proj2.py
- web page: shopper5.html
- DAO: zfood.py
- DB congig: dbconfig.py
- DB config to edit on PA: dbconfigtemplate.py
- Virtual environment requirements: requirements.txt
- Initial plan: ProposedInterface1.docx

- Images in \images
- All early versions in \testing

### How to clone this repository
A repository on GitHub exists as a remote repository. You can clone this repository to create a local copy on your computer by following these instructions:
1. On GitHub, navigate to the main page of the repository https://github.com/elizabethdaly/data-rep-project
2. Under the repository name, click Clone or download.
3. Choose "Clone with HTTPS".
4. Open a terminal on your machine. Change the current working directory to the location where you want the cloned directory to be made.
5. Type git clone, and then paste the URL you copied in 2 above.
```
git clone https://github.com/elizabethdaly/data-rep-project
```
6. Press enter to clone the repository to your machine.

### MySQL database & table

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


### Web page

Started off with basic one provided and gradually added extra:


- Price displayed as two decimal places on initial read from DB and after create & update.
```javascript
parseFloat(food.Price).toFixed(2)
```
- CSS Bootstrap: buttons, form
- Added host code to ajax calls
- Link on page to application on pythonanywhere.

### Servers

Started with basic one provided and added a little to it:

- Allow for decimal type in DB
```python
from decimal import Decimal
```
### DAO
- zfoodDAO.py contains foodDAO class

### Current working version:
- shopper5.html
- server_proj2.py
- zfoodDAO.py

## References/code help
1. [Formatting numbers to 2 decimal places in json](https://stackoverflow.com/questions/30247108/round-all-decimals-from-dynamic-json-to-2-decimal-places)
(Accessed 6 Dec 2019)
2. [Serialize a decimal object in json](https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object/39257479) (Accessed 4 Dec 2019)
3. [Bootstrap](https://getbootstrap.com/docs/3.4/) (last accessed 15 Dec 2019)
4. [W3schools columns](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_three_columns_unequal) (last accessed 15 Dec 2019) for example.