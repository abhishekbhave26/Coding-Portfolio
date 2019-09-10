# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:43:35 2019

@author: abhis
"""

def rankIndex(values, rank):
    x=[]
    for i in values:
        temp=sum(i)
        x.append(temp)
    while(rank>1):
        temp=max(x)
        d=x.index(temp)
        x[d]=-1
        rank-=1
    d=max(x)
    return x.index(d)

a=[[80, 96, 81, 77], [78, 71, 93, 75],[71, 98, 70, 95], [80, 96, 89, 77]] 
k=3
x=rankIndex(a,k)
print(x)