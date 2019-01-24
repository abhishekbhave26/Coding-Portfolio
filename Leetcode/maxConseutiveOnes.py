# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 02:25:02 2019

@author: abhis
"""

#leetcode 485

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count,n=0,0
        for i in nums:
            if(i==0):
                count=0
            else:
                count+=1
                if(n<count):
                    n=count
        return n
                    
                
s=Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,1,1,0,1]))