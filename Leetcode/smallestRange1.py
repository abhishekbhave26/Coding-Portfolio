# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:50:55 2019

@author: abhis
"""

#leetcode 908

class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2*K)
    
s=Solution()
x=s.smallestRangeI([0,10],2)
print(x)        