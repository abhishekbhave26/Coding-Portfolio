# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 18:13:52 2019

@author: abhis
"""

#leetcode 496

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in findNums:
            x=nums.index(i)
            for j in nums[x:]:
                #print(j)
                if(j>i):
                    new.append(j)
                    break
            else:
                new.append(-1)
        return new
    
    
    
    def nextGreaterElement3(self, findNums, nums):
        d={}
        res=[]
        stack=[]
        for i in nums:
            while(len(stack)!=0 and stack[-1] < i ):
                x=stack.pop()
                d[x]=i
            stack.append(i)
                
        #print(d)
        #print(stack)
        for i in findNums:
            x=d.get(i,-1)
            res.append(x)
        return res            
            
        
    
        
s=Solution()
x=s.nextGreaterElement3([2,4], [1,2,3,4])
print(x)