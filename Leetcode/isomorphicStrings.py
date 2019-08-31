# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:47:16 2019

@author: abhis
"""
#leetcode 205

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        h={}
        for i in range(0,len(s)):
            if(s[i] in h and h[s[i]]!=t[i]):
                return False
            if(s[i] not in h and t[i] in h.values()):
                return False
            h[s[i]]=t[i]
        return True
                
    
s=Solution()
print(s.isIsomorphic("paper","title"))
                
        