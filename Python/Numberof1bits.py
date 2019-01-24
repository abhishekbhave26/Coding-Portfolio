# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:34:08 2019

@author: abhis
"""
#leetcode 191

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
        

s=Solution()
n=00000000000000000000000000001011
x=s.hammingWeight(n)
print(x)