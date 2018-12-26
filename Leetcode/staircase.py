# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:43:22 2018

@author: abhis
"""
def staircase(n):
    x=' '
    star='#'
    for i in range(1,n+1):
        print((n-i)*x+((i)*star))

        
staircase(6)