# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 21:42:48 2019

@author: abhis
"""
#leetcode 977

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in range(0,len(A)):
            new.append(A[i]*A[i])
        new.sort()
        return new
                
s=Solution()
x=s.sortedSquares([-7,-3,2,3,11])
print(x)
        
        