'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"product.db")
if cnn:
    print('Tạo và mở CSDL thành công')
    i = 1
    while i:
        cv = int(input('Bạn muốn làm gì? \n1: Hiển thị danh sách sản phẩm \n2: Thêm sản phảm mới \n3: Tìm kiếm sản phẩm theo tên \n4: Cập nhật sản phẩm \n5: Xóa sản phẩm \t'))
        if cv == 1:
            cursor = cnn.execute("SELECT * from PRODUCT")
            for row in cursor:
                print("ID = ",row[0])
                print("NAME = ",row[1])
                print("PRICE = ",row[2])
                print("AMOUNT = ",row[3],"\n")
        elif cv == 2:
            name = input('Nhập tên sản phẩm: ')
            price = int(input('Nhập đơn giá: '))
            amount = int(input('Nhập số lượng: '))
            sql = "INSERT INTO PRODUCT (NAME,PRICE,AMOUNT) VALUES (?,?,?)"
            cnn.execute(sql,(name,price,amount))
            cnn.commit()
            print('Thêm mới thành công')
        elif cv == 3:
            tim = input('Nhập tên sản phẩm: ')
            cursor = cnn.execute("SELECT * from PRODUCT")
            print('Kết quả tìm kiếm:')
            for row in cursor:
                if row[1].lower().find(tim.lower())!=-1:
                    print("ID = ",row[0])
                    print("NAME = ",row[1])
                    print("PRICE = ",row[2])
                    print("AMOUNT = ",row[3],"\n")
        elif cv == 4:
            id_sp = int(input('Nhập id cần cập nhật: '))
            gia_moi = int(input('Nhập đơn giá mới: '))
            so_luong = int(input('Nhập số lượng cần cập nhật: '))
            sql = '''UPDATE PRODUCT SET PRICE = ?, AMOUNT = ? WHERE id = ?'''
            cur = cnn.cursor()
            cur.execute(sql,(gia_moi,so_luong,id_sp))
            cnn.commit()
            print('Cập nhật thành công')
        elif cv == 5:
            cur = cnn.cursor()
            sql = '''DELETE FROM PRODUCT WHERE id = ?'''
            a = input('Nhập id muốn xóa: ')
            cur.execute(sql,(a,))
            cnn.commit()
            print('Xóa thành công')
        i = int(input('Bạn muốn tiếp tục hay không? 1:Có   0:Không  '))  
    cnn.close()
else:
    print('Không mở được CSDL')  