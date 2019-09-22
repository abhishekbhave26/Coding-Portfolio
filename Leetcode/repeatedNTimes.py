# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:18:37 2019

@author: abhis
"""
#leetcode 961

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dic={}
        for i in A:
            if(i in dic):
                return i
            else:
                dic[i]=1
        