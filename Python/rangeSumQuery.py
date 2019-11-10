# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:11:07 2019

@author: abhis
"""
#leetcode 303

#this passes all test cases
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.sum=[0]*(len(self.nums)+1)
        for i in range(0,len(self.nums)):
            self.sum[i+1]=self.sum[i]+self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1]-self.sum[i]




#this solution passes 15/16 test cases
class NumArray2:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, i: int, j: int) -> int:
        res=0
        for x in range(i,j+1):
            res+=self.nums[x]
        return res


#this also passes 15/16 test cases
class NumArray3:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.dic={}
        j=0
        for i in self.nums():
            self.dic[j]=i
            j+=1

    def sumRange(self, i: int, j: int) -> int:
        res=0
        while(i<=j):
            res+=self.dic[i]
            i+=1
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)