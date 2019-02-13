# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 00:11:52 2019

@author: abhis
"""
#leetcode 14

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]f
        
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        print(shortest)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
    
    
s=Solution()
x=s.longestCommonPrefix(["flower","flow","flight"])
        