# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:30:30 2020

@author: abhis
"""

#leetcode 541

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a=list(s)
        for i in range(0,len(a),2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return ''.join(a)
            
        
        
        