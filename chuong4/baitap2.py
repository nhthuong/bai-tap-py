'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"quan_ly_nhan_vien.db")
print('New database is created')
sql = '''CREATE TABLE PHONG (id INTEGER PRIMARY KEY, ten TEXT NOT NULL UNIQUE, chuc_nang TEXT NOT NULL);'''
cnn.execute(sql)
print('Table created successfully')
cnn.close()     