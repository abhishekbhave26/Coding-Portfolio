# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:12:31 2020

@author: abhis
"""

#leetcode 1078

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        if not text:
            return res
        x = text.split()
        for i in range(0,len(x)-2):
            if x[i] == first and x[i+1] == second:
                res.append(x[i+2])
                
        return res
            