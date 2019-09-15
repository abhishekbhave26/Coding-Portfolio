# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:31:13 2018

@author: abhis
"""
#leetcode 238 
#product of all except self

class Solution:
    def productExceptSelf(self, nums):
        N = len(nums)
        output = [1] * N
        p = 1
        for i in range(1,N):
            p = p * nums[i-1]
            output[i] *= p
        p = 1
        for i in range(N-2,-1,-1):
            p = p * nums[i+1]
            output[i] *= p
        return output
    
    def productExceptSelf2(self, nums):
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(length):
            answer[i] = L[i] * R[i]
        return answer
    
    
s=Solution()
print(s.productExceptSelf([3,2,1,7]))