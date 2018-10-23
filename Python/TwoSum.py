# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 22:02:49 2018

@author: abhis
"""
#leetcode 1 

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        '''    
        n^2 solution
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    list.append(i)
                    list.append(j)
                    return list 
        '''
        list=[]
        for i in range(0,len(nums)):
            new=target-nums[i]
            if new in nums[i+1:]:
                list.append(i)
                if(new==nums[i]):
                    x=nums[i+1:].index(new)
                    list.append(x+1)
                    return list
                else:
                    x=nums.index(new)
                    list.append(x)
                    return list
            
s=Solution()
n=[2,5,5,11]
print(s.twoSum(n,10))