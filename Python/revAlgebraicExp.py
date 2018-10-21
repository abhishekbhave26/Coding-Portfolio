# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 16:15:55 2018

@author: abhis
"""

def reverse(expression):
    
    s=expression
    n=len(expression)
    rest=''
    rev=''
    list=[]
    for i in (range(0,n)):
        if(s[i] == '+' or s[i] == '-' or s[i] == '/' or s[i] == '*'):
            if(s[i+1]=='-'):
               temp=str(s[i])+str(s[i+1])+rest
               list.append(temp)  
               rest=''
               i+=1
                
            else:
                temp=str(s[i])+rest
                list.append(temp)  
                rest=''
        else:
            rest=rest+str(s[i])
    list.append(rest)
    
    r=len(list)
    list.reverse()
    for i in range(0,r):
        rev=rev+str(list[i])
    return rev
    

print(reverse(4*8+9-8*-777))

