# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 17:20:39 2019

@author: abhis
"""

def electionWinner(votes):
    d={}
    for i in votes:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
            
    
    x=[key for m in [max(d.values())] for key,val in d.items() if val == m]
    x.sort(reverse=True)
    return x[0]
    
    
    
x=['Alex','Michael','Harry','Dave','Michael','Victor','Harry','Alex','Mary','Mary']
y=electionWinner(x)
print(y)