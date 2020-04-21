# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 12:59:19 2018

@author: abhis
"""
class Solution:
    
    #O(log n) binary search soln
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        while(l<r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid
        return l

    
    
    #O(n) soln
    def searchInsert2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        t=nums[0]
        i=0
        n=len(nums)
        for i in range(t,n):
            if(nums[i]==target):
                print('hello')
                return i
            elif(nums[i]>=target):
                
                i=i-1
                return i
            elif(i==n-1):
                i+=1
                return i
            else:
                pass
                
            
                
                
                

nums=[1,3,5,6]
print(Solution.searchInsert(Solution,nums,4))
            