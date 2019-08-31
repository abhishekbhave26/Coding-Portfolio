# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 01:20:26 2019

@author: abhis
"""
#leetcode 219

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        counts = {}
        for i, v in enumerate(nums):
            if v in counts:
                if i - counts[v] <= k:
                    return True
                else:
                    counts[v] = i
            else:
                counts[v] = i
        return False
    
s=Solution()
print(s.containsNearbyDuplicate([1,4,6,3,5,3,6],2))