# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 00:52:05 2018

@author: abhis
"""
#leetcode 349

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in range(0,len(nums1)):
            if(nums1[i] in nums2 and nums1[i] not in new):
                new.append(nums1[i])
                
        return new
    
s=Solution()
print(s.intersection([1,2,2,1],[2,2]))