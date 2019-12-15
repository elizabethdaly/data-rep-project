# For interaction with Table = food in Database = datarepresentation
# Modify zstudentDAO -> zfoodDAO
#
# pip install mysql-connector-python
# NOT
# pip install mysql-connector
# https://stackoverflow.com/questions/34168651/what-are-the-differences-between-mysql-connector-python-mysql-connector-python

import mysql.connector
import dbconfig as cfg

# Change class name here
class FoodDAO:
    db = ""
    
    #def __init__(self):
    def connectToDB(self):
        self.db = mysql.connector.connect(
        host = cfg.mysql['host'],
        user = cfg.mysql['user'],
        password = cfg.mysql['password'],
        database = cfg.mysql['database']
        )
    
    def __init__(self):
        self.connectToDB()

    # Check for cnxn, if none make one.
    def getCursor(self):
        if not self.db.is_connected():
            self.connectToDB()
        return self.db.cursor()


    def create(self, values):
        cursor = self.getCursor()
        sql = "insert into food (category, name, price) values (%s, %s, %s)"
        cursor.execute(sql, values)

        self.db.commit()
        lastRowID = cursor.lastrowid
        cursor.close()
        return lastRowID
        print("create done")

    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from food"
        cursor.execute(sql)
        results = cursor.fetchall()

        # Formatting what comes back from DB
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        cursor.close()
        return returnArray
        print("get all done")

    def findByID(self, id):
        cursor = self.getCursor()
        sql = "select * from food where id = %s"
        values = (id, )

        cursor.execute(sql, values)
        result = cursor.fetchone()
        # Format what comes back from db
        food = self.convertToDictionary(result)

        cursor.close()  
        return food

    def update(self, values):
        cursor = self.getCursor()
        sql = "update food set category = %s, name = %s, price = %s where id = %s"
        
        cursor.execute(sql, values)
        self.db.commit()
        print("update done")
        cursor.close()

    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from food where id = %s"
        values = (id, )

        cursor.execute(sql, values)
        self.db.commit()
        print("delete done for id", id)
        cursor.close()

    # Converting tuple returned from DB into dict
    def convertToDictionary(self, result):
        
        # List of attributes - match html with colnames
        colnames = ['id', 'Category', 'Name', 'Price']
        
        # Empty list
        item = {}

        # Can't enumerate through an empty result, so check.
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value

        return item

foodDAO = FoodDAO()

