# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 12:42:14 2019

@author: abhis
"""
#leetcode 60

from itertools import permutations
import math
class Solution:
    #my soln
    def getPermutation2(self, n, k):
        x=[]
        for i in range(1,n+1):
            x.append(i)
        c=list(permutations(x))
        a=list(c[k-1])
        s=''
        for i in a:
            s+=str(i)
        return s
    
    def getPermutation(self, n, k):
        self.nums = []
        k -= 1
        ans =""
        for i in range(1,n+1):
            self.nums.append(str(i))
        for n_ in range(1,n+1):
            idx, num = self.helper(n,k,n_)
            ans = ans + num
            k = k - idx * math.factorial(n - n_)   
        return ans
            
    def helper(self,n,k,j):
        idx = k//math.factorial(n-j) 
        return idx, self.nums.pop(idx)