# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:45:56 2019

@author: abhis
"""
#leetcode 198

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i,e=0,0
        for k in range(0,len(nums)):
            tmp = i
            i = nums[k] + e
            e = max(tmp, e)
        
        return max(i,e)
        
s=Solution()
x=s.rob([1,5,3,2,2,3,55,2])
print(x)