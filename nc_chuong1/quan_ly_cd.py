'''
Created on May 19, 2018

@author: hv
'''

class DiaCD(object):
    '''
    classdocs: Quản lý CD
    '''
    tong_tien = 0

    def __init__(self, ten, ca_sy, so_bai_hat, gia_thanh):
        '''
        Constructor
        '''
        self.ten = ten
        self.ca_sy = ca_sy
        self.so_bai_hat = so_bai_hat
        self.gia_thanh = gia_thanh
        DiaCD.tong_tien += self.gia_thanh
        
    def thong_tin_CD(self):
        return('# ' + self.ten + ' - ' + self.ca_sy + ' - '\
               + str(self.so_bai_hat) + ' - ' + str(self.gia_thanh))

if __name__ == '__main__':
    list_cd = []
    i = 1
    while i:
        ten = input('Nhập tên CD: ')
        ca_sy = input('Nhập tên ca sỹ: ')
        so_bai_hat = int(input('Nhập số bài hát: '))
        gia_thanh = eval(input('Nhập giá thành: '))
        cd = DiaCD(ten,ca_sy,so_bai_hat,gia_thanh)
        list_cd.append(cd)
        print('-- Danh sách CD --')
        for item in list_cd:        
            print(item.thong_tin_CD())
        print('Tổng giá thành: ',DiaCD.tong_tien)        
        i = int(input('Tiếp tục nhập? 1:có 0:không '))
