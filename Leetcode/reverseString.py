# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:07:03 2020

@author: abhis
"""

#leetcode 344

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        while(l<r):
            s[l],s[r] = str(s[r]),str(s[l])
            l+=1
            r-=1
        