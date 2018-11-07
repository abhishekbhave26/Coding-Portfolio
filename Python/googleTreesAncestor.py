# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:29:39 2018

@author: abhis
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(D, A):
    result=[]
    # write your code in Python 3.6
    for i in range(0,len(A)):
        
        if(i==0):
            result.append(-1)
        elif(i-D<0):
            result.append(-1)
        else:
            result.append(i-D)
    
    print(result)
    
    
solution(2,[-1,0,1,2,3])