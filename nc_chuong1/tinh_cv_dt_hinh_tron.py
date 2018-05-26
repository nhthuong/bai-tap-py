'''
Created on May 19, 2018

@author: hv
'''
import math

class HinhTron(object):
    '''
    classdocs: Tính chu vi, diện tích hình tròn
    '''


    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
    def tinh_chu_vi(self,B):
        r = math.sqrt((self.x-B.x)*(self.x-B.x)+(self.y-B.y)*(self.y-B.y))
        return 2*3.14*r
    
    def tinh_dien_tich(self,B):
        r = math.sqrt((self.x-B.x)*(self.x-B.x)+(self.y-B.y)*(self.y-B.y))
        return 3.14*math.pow(r,2)
    
if __name__ == '__main__':
    Ox = int(input('Nhập Ox: '))
    Oy = int(input('Nhập Oy: '))
    O = HinhTron(Ox,Oy)
    Rx = int(input('Nhập Rx: '))
    Ry = int(input('Nhập Ry: '))
    R = HinhTron(Rx,Ry)
    
    print('Chu vi = ',HinhTron.tinh_chu_vi(O, R))
    print('Diện tích = ',HinhTron.tinh_dien_tich(O, R))