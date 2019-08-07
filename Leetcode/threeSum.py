# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 23:24:03 2019

@author: abhis
"""
#leetcode 15

from itertools import combinations 
 
class Solution:
    def threeSum(self, nums):
        res=[]
        dic=[]
        l = list(combinations(nums,3))
        for i in l:
            s=list(i)
            g=set(s)
            if(sum(s)==0 and g not in dic):
                res.append(s)
                dic.append(g)
        return res