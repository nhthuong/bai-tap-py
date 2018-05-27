'''
Created on May 27, 2018

@author: hv
'''
class DonVi(object):
    '''
    classdocs Đơn vị
    '''


    def __init__(self, iddv, ten):
        '''
        Constructor
        '''
        self.iddv = iddv
        self.ten = ten
class NhanVien(object):
    '''
    classdocs Nhân viên
    '''
    def __init__(self, idnv, ho_ten, gioi_tinh, ngay_sinh, cmnd, muc_luong, dia_chi, iddv):
        self.idnv = idnv
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.ngay_sinh = ngay_sinh
        self.cmnd = cmnd
        self.muc_luong = muc_luong
        self.dia_chi = dia_chi
        self.iddv = iddv
        
    def in_thong_tin(self):
        gioi_tinh = "";
        if self.gioi_tinh == 'true':
            gioi_tinh = 'nam'
        else:
            gioi_tinh = 'nữ'
        return self.idnv + '-' + self.ho_ten + '-' + gioi_tinh + '-' + self.ngay_sinh + '-' + self.cmnd + '-' + self.muc_luong + '-' + self.dia_chi