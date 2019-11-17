# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 19:05:14 2019

@author: abhis
"""
#leetcode 33

class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        for i,v in enumerate(nums):
            if(v==target):
                return i
        return -1
    
    def search(self, nums, target):
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
        