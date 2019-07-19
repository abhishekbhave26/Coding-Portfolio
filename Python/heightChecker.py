# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 00:56:43 2019

@author: abhis
"""
#leetcode 1051

class Solution:
    def heightChecker(self, heights):
        temp=sorted(heights)
        ans=0
        for i in range(0,len(temp)):
            if(temp[i]!=heights[i]):
                ans+=1
        return ans
    
s=Solution()
print(s.heightChecker([1,3,5,2,3]))