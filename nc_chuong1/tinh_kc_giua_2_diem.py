'''
Created on May 19, 2018

@author: hv
'''
import math

class Diem(object):
    '''
    classdocs: Phép tinh cộng, trừ, nhân, chia
    '''


    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
    def tinh_khoang_cach(self, B):
        return math.sqrt((self.x-B.x)*(self.x-B.x)+(self.y-B.y)*(self.y-B.y))
    
if __name__ == '__main__':
    Ax = int(input('Nhập Ax = '))
    Ay = int(input('Nhập Ay = '))
    A = Diem(Ax,Ay)
    Bx = int(input('Nhập Bx = '))
    By = int(input('Nhập By = '))
    B = Diem(Bx, By)
    print('Khoảng cách giữa A & B: ',A.tinh_khoang_cach(B))