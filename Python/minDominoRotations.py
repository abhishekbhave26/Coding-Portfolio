# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:54:18 2019

@author: abhis
"""

#leetcode 1007

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if(len(A)!=len(B)):
            return -1
        hmapA,hmapB,dic=[0]*7,[0]*7,[0]*7
        for i in range(0,len(A)):
            hmapA[A[i]]+=1
            hmapB[B[i]]+=1
            if(A[i]==B[i]):
                dic[A[i]]+=1
        for i in range(1,7):
            if(hmapA[i]+hmapB[i]-dic[i]>=len(A)):
                return min(hmapA[i],hmapB[i])-dic[i]
        return -1


