# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 00:24:07 2019

@author: abhis
"""
#leetcode 75

class Solution:
    
    def sortColors(self, nums):
        color_dict = {}
        for num in nums:
          if num in color_dict:
            color_dict[num] += 1
          else:
            color_dict[num] = 1

        idx = 0
        if(0 in color_dict):
            for i in range(color_dict[0]):
              nums[idx] = 0
              idx += 1
        if(1 in color_dict):
            for i in range(color_dict[1]):
              nums[idx] = 1
              idx += 1
        if(2 in color_dict):
            for i in range(color_dict[2]):
              nums[idx] = 2
              idx += 1
        
class Solution2:
    
    def sortColors(self, nums):
        p0 = curr = 0
        p2 = len(nums) - 1

        while curr <= p2:
            
            if nums[curr] == 0:
                # swap p0 with curr
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                # swap p2 with curr
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
        print(nums)
                
s=Solution2()
s.sortColors([0,1,2,2,0,1])