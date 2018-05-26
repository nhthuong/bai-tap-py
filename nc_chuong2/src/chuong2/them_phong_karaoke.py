'''
Created on May 26, 2018

@author: Thuong
'''
import json
from pprint import pprint
print('Nhập thông tin phòng karaoke')
maid = input('Nhập ID: ')
ten = input('Nhập tên: ')
ma_so = input('Nhập nã số: ')
id_loai_phong = input('Nhập ID loại phòng: ')
don_gia = input('Nhập đơn giá: ')
so_khach_toi_da = input('Nhập số khách tối đa: ')
trang_thai = input('Nhập trạng thái (CON_TRONG hoặc CO_KHACH): ')
phong = {'ID':maid,'Ten':ten,'Ma_so':ma_so,'ID_loai_phong':id_loai_phong,'Don_gia':don_gia,'So_khach_toi_da':so_khach_toi_da,'Trang_thai':trang_thai}
list1 = []
list1.append(phong)
new = {ma_so:list1}
f = open('quan_ly_phong_karaoke.json', encoding = "utf-8")
data = json.load(f)
data.update(new)
f = open('quan_ly_phong_karaoke.json', 'w', encoding = "utf-8")
json.dump(data, f, indent=4)
f.close()
print('Đã ghi xong')
f = open('quan_ly_phong_karaoke.json',encoding = "utf-8")
data = json.load(f)
pprint(data)