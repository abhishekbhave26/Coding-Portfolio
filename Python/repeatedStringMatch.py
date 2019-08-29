# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:51:28 2019

@author: abhis
"""
#leetcode 686

class Solution:
    #my soln
    def repeatedStringMatch(self, A, B):
        x=''
        s=int(10000/len(A))
        for i in range(0,s):
            x+=A
            if(B in x):
                return i+1
        return -1
    
    def repeatedStringMatch2(self, A, B):
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q+i): return q+i
        return -1
    
s=Solution()
A = "abcd"
B = "cdabcdab"
x=s.repeatedStringMatch(A,B)
print(x)