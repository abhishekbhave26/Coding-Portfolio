# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:25:34 2018

@author: abhis
"""


def solution(parentheses):
    # Type your solution here 
    pass
    count=0
    new=''
    if(parentheses==''):
        return parentheses
    if(parentheses[0]==')' and len(parentheses)==2):
        new='('+parentheses
    else:
        new=parentheses
    
    for i in new:
        
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    while(count!=0):
        
        if(count>0):
            new=new+')'
            count=count-1
        else:
            new='('+new
            count=count+1
            
    return new
            
x=solution('(()))))((())')
print(x)