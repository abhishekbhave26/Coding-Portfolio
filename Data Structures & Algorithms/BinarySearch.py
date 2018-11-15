# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:28:43 2018

@author: abhis
"""
#leetcode 701 binary search 

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        if(target in nums):
            x=nums.index(target)
            return x
        else:
            return -1
        '''
        length=len(nums)
        right=nums[0]
        left=nums[length-1]
        while(left>=right):
            pass