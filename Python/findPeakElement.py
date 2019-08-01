# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:52:01 2019

@author: abhis
"""
#leetcode 162

class Solution:
    #O(n) solution
    def findPeakElement2(self, nums):
        for i in range(0,len(nums)-1):
            if(nums[i]>nums[i+1]):
                return i
        return len(nums)-1

    #O(log n) solution
    def findPeakElement(self, nums):
        lo=0
        hi=len(nums)-1
        while(lo<hi):
            mid=(lo+hi)//2
            if(nums[mid]>nums[mid+1]):
                hi=mid
            else:
                lo=mid+1
            
        return lo
        
s=Solution()
print(s.findPeakElement([1,2,3,1]))
        