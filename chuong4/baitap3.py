'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"quan_ly_nhan_vien.db")
print('Opened database successfully')
sql1 = "INSERT INTO NHAN_VIEN (ho_ten,tuoi,dia_chi,luong,phong_id) VALUES ('Trần Minh', 32, 'Quận 1', 8500000.00, 1)"
sql2 = "INSERT INTO NHAN_VIEN (ho_ten,tuoi,dia_chi,luong,phong_id) VALUES ('Nguyễn Thương', 28, 'Quận 10', 7500000.00, 1)"
sql3 = "INSERT INTO NHAN_VIEN (ho_ten,tuoi,dia_chi,luong,phong_id) VALUES ('Lê Trang', 25, 'Quận 2', 7000000.00, 2)"
sql4 = "INSERT INTO NHAN_VIEN (ho_ten,tuoi,dia_chi,luong,phong_id) VALUES ('Phan Anh Thư', 23, 'Quận 4', 7830000.00, 2)"
cnn.execute(sql1)
cnn.execute(sql2)
cnn.execute(sql3)
cnn.execute(sql4)
cnn.commit()
cnn.close()