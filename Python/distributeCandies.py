# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 01:34:08 2019

@author: abhis
"""
#leetcode 575

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        seen=set(candies)
        return min(len(seen),len(candies)/2)
    
x=Solution()
print(x.distributeCandies([1000,1,1,1]))