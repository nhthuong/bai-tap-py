'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"company.db")
print('Opened database successfully')
cur = cnn.cursor()
sql = '''DELETE FROM EMPLOYEE WHERE id = ?'''
a = input('Nhập id muốn xóa: ')
cur.execute(sql,(a,))
cnn.commit()
cnn.close()