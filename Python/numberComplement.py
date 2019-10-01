# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:37:32 2019

@author: abhis
"""
#leetcode 476

class Solution:
    def findComplement(self, num: int) -> int:
        temp=bin(num)
        x=''
        flag=0
        for i in str(temp):
            if(flag==1):
                x+=i
            if(i.isalpha()):
                flag=1
        res=''
        for i in str(x):
            if(i=='0'):
                res+='1'
            else:
                res+='0'
        return int(res,2)
            
            
        