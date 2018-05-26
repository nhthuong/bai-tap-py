'''
Created on May 19, 2018

@author: Thuong
'''
import math

class TamGiac(object):
    '''
    classdocs: tam giac
    '''


    def __init__(self, a, b, c):
        '''
        Constructor
        '''
        self.a = a
        self.b = b
        self.c = c
        
    def tinh_chu_vi(self):
        return self.a + self.b + self.c
    
    def tinh_dien_tich(self):
        p = self.tinh_chu_vi()/2
        s = math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        return s
    
    def in_thong_tin(self):
        print('a = ',self.a,'\t','b = ',self.b,'\t','c = ',self.c)
        print('Chu vi: ',self.tinh_chu_vi())
        print('Diện tích: ',self.tinh_dien_tich())
        
def la_tam_giac(a,b,c):
    return a+b>c and a+c>b and b+c>a

if __name__ == '__main__':
    a = eval(input('Nhập a = '))
    b = eval(input('Nhập b = '))
    c = eval(input('Nhập c = '))
    if la_tam_giac(a, b, c):
        tg1 = TamGiac(a,b,c)
        print(tg1.in_thong_tin())
    else:
        print('3 Cạnh không hợp lệ')