# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:47:04 2019

@author: abhis
"""

#leetcode 28

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if(needle not in haystack):
            return -1
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    
s=Solution()
print(s.strStr('ghghgg','gg'))
print(s.strStr('ghghgg','ghghh'))