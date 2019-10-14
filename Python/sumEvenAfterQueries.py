# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 13:46:10 2019

@author: abhis
"""

#leetcode 985

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        S = sum(x for x in A if x % 2 == 0)
        for x,k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            res.append(S)
        return res