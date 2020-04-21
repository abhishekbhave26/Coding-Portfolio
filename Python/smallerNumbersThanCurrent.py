# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:43:27 2020

@author: abhis
"""
#leetcode 1365

class Solution(object):
    # O(N^2) soln 
    def smallerNumbersThanCurrent2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res =[]
        for i in nums:
            count = 0
            for j in nums:
                if i>j:
                    count+=1
            res.append(count)
        return res
    
    # O(NLogN) soln 
    def smallerNumbersThanCurrent(self, nums):
        copy = sorted(nums)
        dic = {}
        for i,v in enumerate(copy):
            if v not in dic:
                dic[v]=i
        return [dic[x] for x in nums]
            
            
        
                