# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:12:56 2019

@author: abhis
"""
def sumOfMultiple():
    result=0
    for i in range(1000):
        if(i % 3 == 0 or i % 5 == 0):
            result+=i
    print(result)
    
sumOfMultiple()