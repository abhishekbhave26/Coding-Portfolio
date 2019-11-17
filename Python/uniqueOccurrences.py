# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:37:17 2019

@author: abhis
"""

#leetcode 1207

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        if(len(set(dic.values()))==len(dic.values())):
            return True
        return False
        