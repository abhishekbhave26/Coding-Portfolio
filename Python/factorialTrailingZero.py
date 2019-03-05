# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:39:08 2019

@author: abhis
"""

#leetcode 172

class Solution:
    def trailingZeroes(self, n):
        count = 0
        start = 5
        while start <= n:
            count = count + n//start
            start = start*5
        return count
    
s=Solution()
print(s.trailingZeroes(5))
        