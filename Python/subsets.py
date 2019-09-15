# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 00:54:41 2019

@author: abhis
"""
#leetcode 78

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res, path = [], []
        def inner(nums, path, res):
            for i, el in enumerate(nums):
                inner(nums[i+1:], path + [el], res)
            res.append(path)
        inner(nums, path, res)
        return res
    
s=Solution()
print(s.subsets([4,6,0]))