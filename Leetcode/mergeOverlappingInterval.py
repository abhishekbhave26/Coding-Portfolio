# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:08:57 2019

@author: abhis
"""
#leetcode 56

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        x=sorted(intervals)
        #print(x)
        for i in x:
            start,end=i[0],i[1]
            if res and res[-1][1]>=start:
                temp=max(end,res[-1][1])
                res[-1]=[res[-1][0],temp]
            else:
                res.append(i)
        return res

