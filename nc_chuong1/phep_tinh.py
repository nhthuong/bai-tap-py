'''
Created on May 19, 2018

@author: hv
'''

class PhepTinh(object):
    '''
    classdocs: Phép tính 2 số
    '''


    def __init__(self, so_thu_nhat, so_thu_hai):
        '''
        Constructor
        '''
        self.so_thu_nhat = so_thu_nhat
        self.so_thu_hai = so_thu_hai
        
    def tong(self):
        return self.so_thu_nhat+self.so_thu_hai
    
    def hieu(self):
        return self.so_thu_nhat-self.so_thu_hai
    
    def tich(self):
        return self.so_thu_nhat*self.so_thu_hai
    
    def thuong(self):
        return self.so_thu_nhat/self.so_thu_hai
    
    def in_ket_qua(self):
        print('Tổng: ',self.tong())
        print('Hiệu: ',self.hieu())
        print('Tích: ',self.tich())
        print('Thương: ',self.thuong())

if __name__ == '__main__':
    so_thu_nhat = eval(input('Nhập số thứ nhất: '))
    so_thu_hai = eval(input('Nhập số thứ hai: '))
    pht = PhepTinh(so_thu_nhat,so_thu_hai)
    pht.in_ket_qua()