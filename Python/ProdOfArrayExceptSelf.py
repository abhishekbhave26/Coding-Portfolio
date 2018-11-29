# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 21:31:13 2018

@author: abhis
"""
#leetcode 238 
#product of all except self

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        new=[]
        newnums=nums
        for i in range(0,len(newnums)):
            copy=newnums
            copy.pop(i)
            prod=copy[0]
            for j in range(1,len(copy)):
                prod*=copy[j]
            new.append(prod)
            print('Hello')
            newnums=nums
        
        return new        
        '''
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
    
    
s=Solution()
print(s.productExceptSelf([3,2,1,7]))