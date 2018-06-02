'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"company.db")
print('Opened database successfully')
cursor = cnn.execute("SELECT * from EMPLOYEE")
for row in cursor:
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("AGE = ",row[2])
    print("ADRESS = ",row[3])
    print("SALARY = ",row[4],"\n")
print('Operation done successfully')
cnn.close()    