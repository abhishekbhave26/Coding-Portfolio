# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:56:32 2019

@author: abhis
"""

def calculateScore(text, prefixString, suffixString):
    pr=0
    sf=0
    y=""
    prF=""
    a,s=text,text
    for i in range(0,len(text)):
        y+=text[i]
        if(y in prefixString):
            pr+=1
            prF+=text[i]
        else:
            break   
    x=""
    z=""
    sfF=""   
    i=len(a)-1
    while(i>=0):
        z+=a[i]
        x=z[::-1]
        print(x)
        if(x in suffixString):
            sf+=1
            sfF+=a[i]
        else:
            break
        i-=1
    sfF=sfF[::-1]
    alist=[]
    total=len(prF)+len(sfF)
    for i in range(len(s)):
        for j in range(i,len(s)):
            y=s[i:j + 1]
            if(len(y)>=total and prF in y and sfF in y):
                alist.append(y)
    x=s
    for i in alist:
        if(i.startswith(prF) and i.endswith(sfF)):
            if(i<x):
                x=i
    return x
                
                
            
        

    
x=calculateScore("nothing","bruno","ingenious")
print(x)