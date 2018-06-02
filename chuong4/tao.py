'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"company.db")
print('New database is created')
sql = '''CREATE TABLE EMPLOYEE (ID INTEGER PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL);'''
cnn.execute(sql)
print('Table created successfully')
cnn.close()