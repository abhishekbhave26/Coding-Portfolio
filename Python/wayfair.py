# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:31:28 2019

@author: abhis
"""

def solution(N):
    # write your code in Python 3.6
    x=str(N)
    final=1
    if(x[0]=='-'):
        final=-1
    ret=[N]
    for i in range(0,len(x)):
        if(x[i].isdigit()):
            temp=x[0:i]
            temp+='5'
            temp+=x[i:]
            #print(temp)
            ret.append(int(temp))
    if(final==-1):
        ret.remove(N)
    return max(ret)
    
    

print(solution(268))
print(solution(670))
print(solution(0))
print(solution(-999))