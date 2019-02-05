# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:29:25 2019

@author: abhis
"""
#leetcode 169

import collections
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=collections.Counter(nums)
        return max(x, key=x.get)
        
        
s=Solution()
x=s.majorityElement([3,2,3])
y=s.majorityElement([3,3,4])
print(x,y)
        
        