# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:00:51 2019

@author: abhis
"""

#leetcode 215

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # 2 different approaches
        
        return heapq.nlargest(k, nums)[-1]
        
        nums.sort()
        x=len(nums)
        return nums[x-k]
        
    
s=Solution()
x=s.findKthLargest([1,2,5,3,6,4,5,2],3)
print(x)