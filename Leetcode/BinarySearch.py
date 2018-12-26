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
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1