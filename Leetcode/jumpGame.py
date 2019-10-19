# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:07:59 2019

@author: abhis
"""

#leetcode 55

class Solution:
    def canJump(self,nums):
        maxNo=0
        i=0
        while(i<=maxNo):
            maxNo=max(maxNo,i+nums[i])
            if(maxNo>=len(nums)-1):
                return True
            i+=1
        return False