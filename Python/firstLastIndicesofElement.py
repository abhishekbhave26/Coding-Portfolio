# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 23:21:43 2019

@author: abhis
"""
#leetcode 34

class Solution:
    #O(n) solution
    def searchRange2(self, nums, target):
        if(target in nums):
            x=nums.index(target)
            copy=nums[::-1]
            y=copy.index(target)
            return [x,len(nums)-y-1]
        else:
            return [-1,-1]
        
    #O(N) solution but slightly faster
    def searchRange3(self, nums, target):
        res=[]
        if target in nums:
            res.append(nums.index(target))
        else:
            res.append(-1)
            res.append(-1)
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]==target):
                res.append(i)
                break
        return res
    
    #O(log N) solution
    def searchRange(self, nums, target):
        pass
    
    def binarySearch(self,nums,target):
        pass

    


class Solution2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # use binary search to find any index of target
        index = self.binarySearch(nums, target)

        if index == -1:
            return [-1,-1]
        
		# scan left and right of target to see how far the target substring goes
        l = r = index
        while l >= 0 and nums[l] == target:
            l -= 1
        while r < len(nums) and nums[r] == target:
            r += 1
        
        return [l+1, r-1]

    def binarySearch(self, nums, target):
        l = 0
        r = len(nums)
        
        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid
            else:
                l = mid+1
        return -1