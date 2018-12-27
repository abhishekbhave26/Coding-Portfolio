# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:09:03 2018

@author: abhis
"""
import collections as c
import itertools

class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        new=[]
        d={}
        for i in range(0,n):
            if(nums[i] in d):
                x=d.get(nums[i])
                x+=1
                d[nums[i]]=x
            else:
                d[nums[i]]=1    
        for i in range(1,n+1):
            if(i not in d):
                new.append(i)
        return new
        
            
    
        
s=Solution()
x=s.findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(x)