# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 01:16:20 2019

@author: abhis
"""
#leetcode 137

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic.keys():
            if dic[i]==1:
                return i
                
s=Solution()
print(s.singleNumber([3,4,5,5,3,3,5]))         
            
        