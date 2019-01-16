# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:46:43 2019

@author: abhis
"""
#leetcode 561

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
    
s=Solution()
x=s.arrayPairSum([1,4,25,3])
print(x)
        