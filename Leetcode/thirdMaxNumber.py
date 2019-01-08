# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:08:40 2019

@author: abhis
"""
#leetcode 414


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=[]
        if(len(nums)<=0):
            return None
        d={}
        n=len(nums)
        while(n>=0):
            x=max(nums)
            if(x not in d):
                result.append(x)
                nums.remove(x)
                d[x]=1
            n-=1
        x=d.items
        
        if(len(result)>2):
            return result[2]
        else:
            return max(result)
    
    def new(self,nums):
        d={}
        for i in nums:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        x=d.items()
        
            
        
            
s=Solution()
x=(s.thirdMax([2,2,3,1]))   
print(s.new([1,2,3,5,5]))    

