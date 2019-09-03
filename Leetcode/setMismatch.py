# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:28:34 2019

@author: abhis
"""
#leetcode 645

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen={}
        res=[]
        for i in nums:
            if i in seen:
                res.append(i)
            seen[i]=1
        for i in range(1,len(nums)+1):
            if(i not in seen):
                res.append(i)
        return res
        