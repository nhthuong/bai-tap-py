'''
Created on May 19, 2018

@author: hv
'''

class PhuongTrinhBac1(object):
    '''
    classdocs: Giải phương trình bậc 1
    '''


    def __init__(self, a, b):
        '''
        Constructor
        '''
        self.a = a
        self.b = b
                
    def giai_pt(self):
        if self.a==0 and self.b==0:
            return 'Phương trình vô số nghiệm.'
        elif self.a==0 and self.b!=0:
            return 'Phương trình vô nghiệm'
        else:
            return -self.b/self.a
        
    def in_thong_tin(self):
        print('Kết quả: ',self.giai_pt())    
            
if __name__ == '__main__':
    a = eval(input('Nhập a: '))
    b = eval(input('Nhập b: '))
    pt = PhuongTrinhBac1(a,b)
    pt.in_thong_tin()
    