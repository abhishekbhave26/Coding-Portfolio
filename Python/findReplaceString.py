# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:19:25 2020

@author: abhis
"""

#leetcode 833

class Solution(object):
    # attempt , only passes 33/52 cases
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = S
        for i,v in enumerate(sources):
            if S[indexes[i]:indexes[i]+len(v)].startswith(v):
                res = res.replace(v, targets[i],1)
        return res
    
    def findReplaceString2(self, S, indexes, sources, targets): 
        modified = list(S)
        for index, source, target in zip(indexes, sources, targets):
            if S[index:].startswith(source):
                modified[index] = target
                for i in range(index+1, len(source) + index):
                    modified[i] = ""

        return "".join(modified)

                    
                    