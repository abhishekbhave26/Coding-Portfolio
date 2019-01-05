# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:16:18 2019

@author: abhis
"""

class Solution():
    
    def add(self,x,y):
        return x+y
    
    def subtract(self,x,y):
        return x-y
    
    def multiply(self,x,y):
        return x*y
    
    def divide(self,x,y):
        if(y==0):
            raise ValueError('Cannot divide by zero')
        return x/y

s=Solution()