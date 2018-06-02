'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"product.db")
print('New database is created')
sql = '''CREATE TABLE PRODUCT (ID INTEGER PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, PRICE REAL NOT NULL, AMOUNT INT NOT NULL);'''
cnn.execute(sql)
print('Table created successfully')
cnn.close()