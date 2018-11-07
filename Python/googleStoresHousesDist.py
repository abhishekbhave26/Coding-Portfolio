# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:10:20 2018

@author: abhis
"""
import time

start=time.time()
def solution(stores, houses):
    # write your code in Python 3.6
    new=[]
    stores.sort()
    
    for i in range(0,len(houses)):
        a=houses[i]
        newlist=[]
        
        for j in range(0,len(stores)):
            newDist=abs(stores[j]-a)
            newlist.append(newDist)
            if(newDist==0):
                break
            
        x=min(newlist)
        element=newlist.index(x)
        #print(element)
        y=stores[element]
        new.append(y)
    return new

x=solution([1,5,20,11,16],[20,4,0])
print(x)
        
end=time.time()
print(end-start)