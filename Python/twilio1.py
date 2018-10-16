# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 21:36:56 2018

@author: abhis
"""

# read the string filename
filename = open('twilio.txt','r') 
#filename = input('twilio.txt')
dict={}
for i in filename:
    print(i)
    a=0
    for type in i:
        
        while(type!='-'):
            a=str(a+type)
    if('a' in dict):
        count=dict.get('a')
        count+=1
        dict.update(a=count)
    else:
        dict['a']=1


print(dict)

for 