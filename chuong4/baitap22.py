'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"quan_ly_nhan_vien.db")
sql = '''CREATE TABLE NHAN_VIEN (id INTEGER PRIMARY KEY, ho_ten TEXT NOT NULL, tuoi INTEGER NOT NULL, dia_chi TEXT NOT NULL, luong REAL, phong_id INTEGER NOT NULL, FOREIGN KEY(phong_id) REFERENCES PHONG(id));'''
cnn.execute(sql)
cnn.close()