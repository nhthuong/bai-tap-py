'''
Created on May 26, 2018

@author: Thuong
'''
import json
from pprint import pprint
from chuong2.thu_vien import doc_noi_dung_json

if __name__ == '__main__':
    noi_dung = doc_noi_dung_json("QLCT_1.json")
    cong_ty = noi_dung['CONG_TY']
    print('Tên công ty:',cong_ty[0]['Ten'])
    print('Địa chỉ: ',cong_ty[0]['Dia_chi'])
    don_vi = noi_dung['DON_VI']
    tong_nv = 0
    for item in don_vi:
        tong_nv += int(item['So_Nhan_vien'])
    print('Tổng số nhân viên: ',tong_nv)
    print('Thống kê nhân viên theo đơn vị')
    i = 1
    for item in don_vi:
        print(i,'\ Tên đơn vị: ',item['Ten'])
        print('\t - Số nhân viên: ',item['So_Nhan_vien'])
        print('\t - Tỷ lệ: ',item['Ty_le'])
        i+=1