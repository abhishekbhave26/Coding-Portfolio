# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 01:15:50 2019

@author: abhis
"""
#leetcode 88

class Solution:
    def merge(self, nums1,nums2):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(0,len(nums1)):
            if(len(nums2)==0):
                break
            for j in range(0,len(nums2)+1):
                if(nums2[j]<nums1[i]):
                    nums1.insert(i,nums2[j])
                    i+=2
                    nums1.pop()
                    nums2.pop(j)
                    break
                elif nums1[i]==0:
                    nums1[i]=nums2[j]
                    nums2.pop(j)
                    break
                else:
                    break
        return nums1.sort()

s=Solution()
result=s.merge([1],[])

            