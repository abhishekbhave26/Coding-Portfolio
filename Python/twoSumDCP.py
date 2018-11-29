# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 20:38:13 2018

@author: abhis
"""

def sum(list,target):
    
    for i in range(0,len(list)):
        x=target-list[i]
        if(x in list[i+1:]):
            return True
    return False

x=sum([10, 15, 3, 7],17)
print(x)