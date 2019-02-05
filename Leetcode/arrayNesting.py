# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 19:29:25 2019

@author: abhis
"""

#leetcode 565

class Solution(object):
    
    
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, step, n = 0, 0, len(nums)
        seen = [False] * n
        for i in range(n):
            while not seen[i]:
                seen[i] = True
                i, step = nums[i], step + 1
            ans = max(ans, step)
            step = 0
        return ans    
    
    
    #passes only 600 test cases
    def arrayNesting2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        
        count=0
        for i in range(0,len(nums)):
            d[i]=nums[i]
        new={}
        for i in range(0,len(nums)):
        
            x=d[i]
            y=0
            while(y not in new):
                new[x]=1
                y=d[x]
                x=y
            
            ma=len(new)
            if(ma>count):
                count=ma
        return ma
            
s=Solution()
x=s.arrayNesting([0,2,1])
print(x)