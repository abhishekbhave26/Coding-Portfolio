# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:55:05 2019

@author: abhis
"""

def compressedString(message):
    # Write your code here
    count=1
    x=message[0]
    i=0
    while(i<len(message)-1):
        if(message[i]==message[i+1]):
            count+=1
        else:
            if(count>1):
                x+=str(count)
            x+=message[i+1]
            count=1
        i+=1
    if(count>1):
        x+=str(count)
    return x