# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:55:44 2020

@author: abhis
"""

#leetcode 1189

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={}
        count = 0
        for i in text:
            if i in dic:
                dic[i]+=1
            elif i in {'b','a','l','o','n'}:
                dic[i]=1
        while(True):
            if('b' in dic and 'a' in dic and 'l' in dic and 'o' in dic and 'n' in dic):
                if(dic['l']>=2 and dic['o']>=2):
                    dic = helper(dic,'b',1)
                    dic = helper(dic,'a',1)
                    dic = helper(dic,'l',2)
                    dic = helper(dic,'o',2)
                    dic = helper(dic,'n',1)
                    count+=1
                    continue
            break
                
        return count
    
def helper(dic,char,count):
    if dic[char]>count:
        dic[char]-=count
    else:
        del dic[char]            
    return dic
        