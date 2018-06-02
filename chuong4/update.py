'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"company.db")
print('Opened database successfully')
cur = cnn.cursor()
sql = '''UPDATE EMPLOYEE SET SALARY = ? WHERE id = ?'''
a = int(input('Nhập id cần cập nhật: '))
b = int(input('Nhập lương cần cập nhật: '))
cur.execute(sql,(b,a))
cnn.commit()
cnn.close()