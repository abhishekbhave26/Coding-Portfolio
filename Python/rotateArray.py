# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 20:58:16 2019

@author: abhis
"""
#leetcode 189

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        
        j=len(nums)-1
        #i=0
        if k> len(nums):
            k = k-len(nums)
        for i in range(k):
            j=(len(nums))-1
            temp =nums[j]
            while j>0:                
                nums[j]=nums[j-1]
                j -=1
            nums[0] = temp
        """ 
         
        k = k% len(nums)
        n = len(nums)
        nums[:] = nums[n-k:]+nums[:n-k]
        print(nums)
    
if __name__=="__main__":
    s=Solution()
    print(s.rotate([1,2],1))