# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 21:17:42 2020

@author: abhis
"""
#hackerrank question

def jumpingOnClouds(c):
    i=0
    res =0
    while i < n-1:
        if i+2<n and c[i+2] == 0:
            i = i+2
            res += 1
        else:
            i = i+1
            res += 1
    return res