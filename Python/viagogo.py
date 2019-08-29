# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:25:49 2019

@author: abhis
"""

s="1 1 1 40 60"
d="2 1 4 50"

def process(s):
    a=list(s)
    l=[]
    flag,price=0,0
    g=0
    x,y,cheapestPrice,eventID="","","",""
    for i in a:
        if(i!=" " and x!="" and eventID!="" and y!=""):
            cheapestPrice+=i
            flag=1
            g=1
        elif(i!=" " and x!="" and eventID!=""):
            y+=i
            g=1
        elif(i!=" " and eventID!=""):
            x+=i
            g=1
        if(i!=" " and g==0):
            eventID+=i
        if(i==" " and flag==1):
            price=int(cheapestPrice)
            l.append(price)
            cheapestPrice=""
    if(flag==1):
        price=int(cheapestPrice)
        l.append(price)
        
    return int(eventID),int(x),int(y),min(l)
            
print(process(d))  




if(minDist>a):
    minDist=a
    finalCost=cost
    ID=eID
if(minDist==a and finalCost>cost):
    minDist=a
    finalCost=cost
    ID=eID
if(minDist==a and finalCost==cost):
    minDist=a
    finalCost=cost
    ID=eID
  
    
    
h={3:[(4,5)],4:[(1,3)]}
