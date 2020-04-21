# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:18:35 2020

@author: abhis
"""

# leetcode 239

class Solution(object):
    
    #O(n) soln
    def maxSlidingWindow(self, nums, k):
        res = []
        dq = []
        
        if not nums or k < 1 or k > len(nums):
            return res
        
        for i,v in enumerate(nums):
            
            if dq and dq[0] < i-k+1:
                dq.pop(0)
            
            while dq and nums[dq[-1]] < v:
                dq.pop()
            dq.append(i)
            if i>=k-1:
                res.append(nums[dq[0]])
            print(res,dq,i,v)
                
        return res
            
    
    #O(n^2) soln
    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in range(0,len(nums)-k+1):
            tempSum = nums[i]
            for j in range(i+1,i+k):
                tempSum = max(tempSum, nums[j])
            res.append(tempSum)
        return res
        