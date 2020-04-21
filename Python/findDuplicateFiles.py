# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 00:00:26 2020

@author: abhis
"""
#leetcode 609

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        res = []
        for i in paths:
            x = i.split()
            root = x[0] + '/'
            for j in x[1:]:
                op = j.index('(')
                cl = j.index(')')
                s = j[op+1:cl]
                if s in dic:
                    temp = dic[s]
                    temp.append(root + j[0:op])
                    dic[s] = temp
                else:
                    dic[s] = [root + j[0:op]]
        for j in dic:
            if len(dic[j])>1:
                res.append(dic[j])
        return res
            
            
                    
        