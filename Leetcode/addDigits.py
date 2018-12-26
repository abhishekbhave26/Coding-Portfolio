# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:19:39 2018

@author: abhis
"""
#leetcode 258

#add digits 

class Solution(object):

    def addDigits(self, num):
        while(num>9):
            o=int(num%10)
            t=int(num/10)
            num=o+t
        else:
            return num
        
s=Solution()
print(s.addDigits(38))