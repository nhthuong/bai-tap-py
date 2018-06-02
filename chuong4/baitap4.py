'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"quan_ly_nhan_vien.db")
print('Opened database successfully')

phong = cnn.execute("SELECT * from PHONG")
for row in phong:
    print("ID = ",row[0])
    print("username = ",row[1])
    print("password = ",row[2],"\n")
    
cnn.close()