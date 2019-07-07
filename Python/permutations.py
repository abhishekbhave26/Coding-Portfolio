# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 18:34:10 2019

@author: abhis
"""
#leetcode 46

import itertools

class Solution:
    def permute(self, nums):
        res=[]
        if(len(nums) in [0,1]):
            res.append(nums) 
            return res
        return list(itertools.permutations(nums))
        
    def permute2(self, nums):
        if len(nums) <=1:
            yield nums
        else:
            for i in range(len(nums)):
                for perm in Solution.permute2(Solution,nums[1:]):    
                    yield perm[:i] + nums[0:1] + perm[i:]
                    
                    
s=Solution()
result=s.permute([3,4,5])
print(list(result))

            
            
            
        