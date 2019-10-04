# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:01:47 2019

@author: abhis
"""

sum = 0
for i in range(1,1000):
    if (i%3 == 0 or i%5 == 0):
        sum+=i
print(sum)