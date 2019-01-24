# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 02:48:33 2019

@author: abhis
"""

#leetcode 442

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        new=[]
        for i in nums:
            if i in d:
                d[i]+=1
                new.append(i)
            else:
                d[i]=1
        x=set(new)
        return list(x)
        
s=Solution()
print(s.findDuplicates([1,4,5,3,6,9,2,3,6,5,5,4]))
                
                
        