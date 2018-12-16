# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:07:04 2018

@author: abhis
"""

#leetcode 41

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return 1
        x=max(nums)
        for i in range(1,x+1):
            if(i in nums):
                pass
            else:
                return i
        return x+1;



s=Solution()
print(s.firstMissingPositive([1,-2,3]))

def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n