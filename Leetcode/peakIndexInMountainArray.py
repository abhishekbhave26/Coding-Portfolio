# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 01:04:54 2019

@author: abhis
"""
#leetcode 852

class Solution:
    #O(n) solution Linear Search
    def peakIndexInMountainArray(self, A): 
        if(len(A)<3 or len(A)>10000):
            return -1
        temp=A[0]
        for i in range(1,len(A)):
            if(A[i]<temp):
                return i-1
            temp=A[i]
        return i
    
    #O(log N) complexity  Binary Search
    def peakIndexInMountainArray2(self, A):
        if(len(A)<3 or len(A)>10000):
            return -1
        lo=0
        hi=len(A)-1
        while(lo<hi):
            mid=(lo+hi)//2
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo    
        
            
    
s=Solution()
x=s.peakIndexInMountainArray2([1,4,3,2])
print(x)
        