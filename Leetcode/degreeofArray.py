# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:55:48 2019

@author: abhis
"""
#leetcode 897

import collections
class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=collections.Counter(nums)
        m=max(x,key=x.get)
        count=x[m]
        print(m,count)
        i=0
        #print(count)
        flag=0
        new=[]
        c=0
        while(i<len(nums)):
            
            if flag==1 and nums[i]==m:
                c+=1
            elif flag==0 and nums[i]==m:
                c+=1
                flag=1
            elif flag==1:
                c+=1
            i+=1
        return c
    
    
    
    def findShortestSubArray2(self, nums):
        nums_map, deg, min_len = collections.defaultdict(list), 0, float('inf')
        print(nums_map)
        for index, num in enumerate(nums):
            nums_map[num].append(index)
            if len(nums_map[num]) == deg:
                min_len = min(min_len, nums_map[num][-1] - nums_map[num][0] + 1)
            elif len(nums_map[num]) > deg:
                deg = len(nums_map[num])
                min_len = nums_map[num][-1] - nums_map[num][0] + 1
        return min_len

s=Solution()
print(s.findShortestSubArray2([1, 2, 2, 3, 1]))
#print(s.findShortestSubArray([1,2,2,3,1,4,2]))
                
            
        