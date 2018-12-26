# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:07:50 2018

@author: abhis
"""

def birthdayCakeCandles(ar):
    max=ar[0]
    ar.sort()
    for i in range(1,len(ar)):
        if(ar[i]>max):
            max=ar[i]
    count=0
    for i in range(0,len(ar)):
        if(ar[i]==max):
            count+=1
    return count
        
x=[4,3,1,4,1,4]
print(birthdayCakeCandles(x))