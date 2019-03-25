# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:39:40 2019

@author: abhis
"""


def perfectSub(s, k):
    if(s=='' or k==0):
        return 0
    n=0
    d=list(set(s))
    a = []
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            x=(s[i:j+1])   
            if(len(x)>=k and len(x)<=(k*len(d))):
                a.append(x)   
    for i in a:
        flag=0
        for j in d:
            if(j in i):
                t=i.count(j)  
                if(t!=k):
                    flag=1
                    break
        if(flag==0):
            n+=1        
    return n


print(perfectSub('1020122',2))
print(perfectSub('1102021222',2))
print(perfectSub('1221221121',3))