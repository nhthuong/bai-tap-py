'''
Created on May 26, 2018

@author: Thuong
'''
from chuong2.thu_vien import read_json_from_internet_unicode

if __name__ == '__main__':
    url1 = 'http://dev-er.com/service_api_ban_sach/api_service_sach.php'
    noi_dung = read_json_from_internet_unicode(url1)
    print('Tổng sách: ',len(noi_dung))
    print('Danh sách các sách:')
    i = 1
    for item in noi_dung:
        print(i,'/ ',item['ten_sach'], ', Ngày xuất bản: ',item['ngay_xuat_ban'], ', Giá bìa: ',item['gia_bia'])
        i+=1