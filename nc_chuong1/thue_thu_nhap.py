'''
Created on May 19, 2018

@author: hv
'''

class Luong(object):
    '''
    classdocs: Tính lương nhân viên
    '''

    luong_co_ban = 1260000
    def __init__(self, ten, he_so_luong, so_nguoi_giam_tru_gia_canh, phu_cap):
        '''
        Constructor
        '''
        self.ten = ten
        self.he_so_luong = he_so_luong
        self.so_nguoi_giam_tru_gia_canh = so_nguoi_giam_tru_gia_canh
        self.phu_cap = phu_cap
        
    def tinh_thu_nhap(self):
        return self.he_so_luong*Luong.luong_co_ban + self.phu_cap
    
    def tinh_thu_nhap_chiu_thue(self):
        return Luong.tinh_thu_nhap(self) - 9000000 - self.so_nguoi_giam_tru_gia_canh*3600000
    
    def tinh_thue_tncn(self):
        if Luong.tinh_thu_nhap_chiu_thue(self)<5000000:
            return Luong.tinh_thu_nhap_chiu_thue(self)*5/100
        elif Luong.tinh_thu_nhap_chiu_thue<10000000:
            return Luong.tinh_thu_nhap_chiu_thue*1/10
        elif Luong.tinh_thu_nhap_chiu_thue<18000000:
            return Luong.tinh_thu_nhap_chiu_thue*15/100
        elif Luong.tinh_thu_nhap_chiu_thue<32000000:
            return Luong.tinh_thu_nhap_chiu_thue*1/5
        elif Luong.tinh_thu_nhap_chiu_thue<52000000:
            return Luong.tinh_thu_nhap_chiu_thue*1/4
        elif Luong.tinh_thu_nhap_chiu_thue<80000000:
            return Luong.tinh_thu_nhap_chiu_thue*3/10
        else:
            return Luong.tinh_thu_nhap_chiu_thue*35/100
        
    def thuc_linh(self):
        return Luong.tinh_thu_nhap(self) - Luong.tinh_thue_tncn(self)
    
if __name__ == '__main__':
    ten = input('Họ tên: ')
    he_so_luong = eval(input('Hệ số lương: '))
    so_nguoi_giam_tru_gia_canh = int(input('Số người giảm trừ gia cảnh: '))
    phu_cap = eval(input('Phụ cấp: '))
    tn = Luong(ten,he_so_luong,so_nguoi_giam_tru_gia_canh,phu_cap)
    print('Thu nhập: ',tn.tinh_thu_nhap())
    print('Thu nhập chịu thuế: ',tn.tinh_thu_nhap_chiu_thue())
    print('Thuế thu nhập cá nhân: ',tn.tinh_thue_tncn())
    print('Thực lĩnh: ',tn.thuc_linh())