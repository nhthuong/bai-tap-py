'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"quan_ly_nhan_vien.db")
print('New database is created')
sql1 = "INSERT INTO PHONG (ten,chuc_nang) VALUES ('Hành chính', 'Giải quyết các công việc hành chính của công ty')"
sql2 = "INSERT INTO PHONG (ten,chuc_nang) VALUES ('Kỹ thuật', 'Thực hiện các dự án kỹ thuật của công ty')"
cnn.execute(sql1)
cnn.execute(sql2)
cnn.commit()
cnn.close()