'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"quan_ly_nhan_vien.db")
print('Opened database successfully')

phong = cnn.execute("SELECT * from PHONG")
nhan_vien = cnn.execute("SELECT * from NHAN_VIEN")

list_nv = []
list_phong = []
for row in phong:
    list_phong.append(row)
for row in nhan_vien:
    list_nv.append(row)

for row in list_phong:
    print('--- ID = ',row[0],'- Tên:',row[1])
    for nv in list_nv:
        if nv[5] == row[0]:
            print('ID = ', nv[0],'- Tên:',nv[1],'- Tuổi:',nv[2],'- Địa chỉ:',nv[3],'- Lương:',nv[4])
print('Operation done successfully')
cnn.commit()
cnn.close()