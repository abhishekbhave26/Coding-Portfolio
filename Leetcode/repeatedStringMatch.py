# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:51:28 2019

@author: abhis
"""
#leetcode 686

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        x=''
        s=int(10000/len(A))
        for i in range(0,s):
            x+=A
            if(B in x):
                return i+1
        return -1
    
s=Solution()
A = "abcd"
B = "cdabcdab"
x=s.repeatedStringMatch(A,B)
print(x)