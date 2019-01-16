# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 10:54:00 2019

@author: abhis
"""
#leetcode 453


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        x=sum(nums)-min(nums)*len(nums)
            
        return x
    
    
s=Solution()
x=s.minMoves([1,2,3])
print(x)
            
        