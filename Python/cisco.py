# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:29:57 2020

@author: abhis
"""

def find_hidden_string(input_string):
    # Write your code here
    res = []
    for i in range(0,len(input_string)):
        for j in range(i,len(input_string)):
            x=input_string[i:j+1]
            if x==x[::-1]:
                if len(x)>1:
                    res.append(x)
    if len(res)>1:
        res.sort()
    if res: 
        return res[0]
    else:
        return 'None'


#print(find_hidden_string('BCCB'))
        

def get_choco_max(jarray):
    # Write your code here
    withPrev = woPrev = 0
    for i in jarray:
        temp=max(withPrev,woPrev)
        withPrev = woPrev +i
        woPrev = temp
    return max(withPrev,woPrev) 


def stockPairs(stocksProfit, target):
    # Write your code here
    disPairs = []
    dic = {}
    for i in stocksProfit:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in dic:
        if target-i in dic:
            if i ==target-i:
                if dic[i]>1:
                    disPairs.append((i,target-i))
                    dic[i] -=2
            else:
                if dic[target-i]>0 and dic[i]>0:
                    disPairs.append((i,target-i))
                    dic[i] -=1
                    dic[target-i]-=1
    return disPairs

#print(stockPairs([6,12,3,9,3,5,1],12))
    

a='julia1_@hackerrank.com'
x= '^[a-z]{1,6}[_]{0,1}[0-9]{0,4}[@]{1}hackerrank[.]{1}com$'
import re
print(re.search(x,a))