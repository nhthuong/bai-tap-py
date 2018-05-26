'''
Created on May 19, 2018

@author: hv
'''
import math

class HinhChuNhat(object):
    '''
    classdocs: Tính chu vi, diện tích hình chữ nhật
    '''


    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
    def tinh_chu_vi(self,B):
        r = math.sqrt((self.x-B.x)*(self.x-B.x)+(self.y-B.y)*(self.y-B.y))
        return 