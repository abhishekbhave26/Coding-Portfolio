# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:43:37 2019

@author: abhis
"""
#leetcode 190

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x=bin(n)
        x=x[2:]
        print(x)
        y=x[::-1]
        y=int(y)
        return x
        
s=Solution()
x=s.reverseBits(00000010100101000001111010011100)
print(x)