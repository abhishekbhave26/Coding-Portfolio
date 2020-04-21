# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:14:28 2020

@author: abhis
"""

input_list = [ [1,2,3,4], [5,6], [7,8,9,10,11,12]]
def round_robin_order_print(input_list):
    maxLength=-1
    for i in input_list:
        maxLength=max(maxLength,len(i))
    c=0
    while(True):
        for inner_list in input_list:
            if(c<len(inner_list)):
                print(inner_list[c])
            else:
                continue
        c+=1
        if(c>=maxLength):break
    
    
round_robin_order_print(input_list)


inputList=[1,2,3,4]
res=[[]]
#for i in inputList:
#    temp=res
#    for j in res:
#        temp.append(i)
#    res+=temp
print(res)
