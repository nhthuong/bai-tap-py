'''
Created on Mar 16, 2017

@author: KTPHUONG
'''
# import pdb
import json
from time import gmtime, strftime
from chuong2.thu_vien import doc_noi_dung_json
from pprint import pprint
from textwrap import indent

class GiaoDich(object):
    '''
    classdocs: class GiaoDich
    ''' 

    def __init__(self, ma, ngay, don_gia, so_luong, loai):
        '''
        Constructor
        '''
        self.ma = ma
        self.ngay = ngay
        self.don_gia = don_gia
        self.so_luong = so_luong
        self.loai = loai
     
    def thanh_tien(self):        
        return self.so_luong * self.don_gia
    
    def in_giao_dich(self):
        return self.ma + " - " + self.ngay + " - " + self.loai + " - " + str(self.so_luong) \
            + " - " + str(self.don_gia) + " - Thành tiền = " + str(self.thanh_tien())
    
    
class GiaoDichTienTe(GiaoDich):
    '''
    classdocs: class GiaoDichTienTe kế thừa từ lớp giao dịch
    ''' 
        
    def __init__(self, ma, ngay, don_gia, so_luong, loai, mua):
        '''
        Constructor
        '''
        self.mua = mua
        GiaoDich.__init__(self, ma, ngay, don_gia, so_luong, loai)
        
        
    def thanh_tien(self):
        if self.mua:          
            return GiaoDich.thanh_tien(self)
        else:           
            return GiaoDich.thanh_tien(self) * 1.05
    
    def in_giao_dich(self):
        if self.mua:
            return "GD mua: " + GiaoDich.in_giao_dich(self)
        else:
            return "GD bán: " + GiaoDich.in_giao_dich(self) 
        

if __name__ == "__main__":
    # pdb.set_trace()
    print("Quản lý giao dịch:")
    list_vang = []
    list_tien = []
    tiep_tuc = 1
    while tiep_tuc == 1:        
        ma = input("Nhập mã GD:\t")
        ngay = input("Nhập ngày GD:\t")
        
        so_luong = int(input("Nhập số lượng:\t"))
        
        
        i = int(input("Chọn loại giao dịch: 1: Vàng, 2: Tiền Tệ:\t"))
        if i == 1:
            tong_slv = 0
            tong_tien_vang = 0
            loai = input("Chọn loai: 18k / 24k / 9999:\t")
            don_gia = eval(input("Nhập đơn giá:\t"))
            gdv = GiaoDich(ma, ngay, don_gia, so_luong, loai)
            list_vang.append(gdv)
            for item in list_vang:
                tong_slv += item.so_luong
                tong_tien_vang += item.thanh_tien()
                print(item.in_giao_dich())        
            print("Tổng số lượng:", tong_slv)
            print("Tổng số tiền:", tong_tien_vang)
        if i == 2:
            tong_slt = 0
            tong_tien_tien = 0
            loai = input("Chọn loai: USD / EUR / AUD:\t")
            don_gia = eval(input("Nhập tỷ giá:\t"))
            mua = True
            gd = int(input("Bạn mua hay bán? 1: mua, 0: bán:\t"))
            if gd == 0:
                mua = False 
            gdtt = GiaoDichTienTe(ma, ngay, don_gia, so_luong, loai, mua)
            list_tien.append(gdtt)
            for item in list_tien:
                tong_slt += item.so_luong
                tong_tien_tien += item.thanh_tien()
                print(item.in_giao_dich())        
            print("Tổng số lượng:", tong_slt)
            print("Tổng số tiền:", tong_tien_tien)
        
        tiep_tuc = int(input("Bạn muốn tiếp tục giao dịch? 1: Có, 0: Không\t"))       
   
    ghi_file = eval(input('Bạn có muốn ghi nội dung vào file .json? 1:có 0:không \t'))
    if ghi_file == 1:
        data = {}
        data['GiaoDich']=[]
        for item in list_vang:
            data['GiaoDich'].append({
                'ma': item.ma,
                'ngay': item.ngay,
                'don_gia': str(item.don_gia),
                'so_luong': str(item.so_luong),
                'loai': str(item.loai)
                }) 
        data['GiaoDichTienTe']=[]
        for item in list_tien:
            data['GiaoDichTienTe'].append({
                'ma': item.ma,
                'ngay': item.ngay,
                'don_gia': str(item.don_gia),
                'so_luong': str(item.so_luong),
                'loai': str(item.loai),
                'mua': str(item.mua)
                }) 
    thoi_gian_ghi = strftime("%Y-%m-%d-%H-%M-%S",gmtime())
    ten_tap_tin = thoi_gian_ghi + ".json"
    f = open(ten_tap_tin, 'w')
    json.dump(data, f, indent = 4)
    f.close()
    print('Đã ghi nội dung vàn tập tin: ',ten_tap_tin)
    print('Nội dung tập tin:')
    nd = doc_noi_dung_json(ten_tap_tin)
    print(nd)