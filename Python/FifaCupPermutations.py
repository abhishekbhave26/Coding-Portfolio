# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 17:01:33 2018

@author: abhis
"""
from itertools import combinations 

def findMaxGoalsProbability(teamGoals):
    comb = combinations(teamGoals, 2) 
    total_count=0
    count=0
    new=[]
    for i in list(comb):
        total_count+=1
        temp=i[0]+i[1]
        new.append(temp)
        
    listtemp=new[0]
    n=len(new)
    for i in range(1,n):
        if(new[i]>listtemp):
            listtemp=new[i]
    count=new.count(listtemp)
    return float(count/total_count)
    
print(findMaxGoalsProbability([1,2,2,3]))
        
    