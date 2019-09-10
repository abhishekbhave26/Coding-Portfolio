# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:04:53 2019

@author: abhis
"""
#leetcode 349

# O(N) solution
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic={}
        res=[]
        for i in nums1:
            dic[i]=1
        for i in nums2:
            if(i in dic):
                res.append(i)
        return list(set(res))

   
# O(N^2) solution
class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in range(0,len(nums1)):
            if(nums1[i] in nums2 and nums1[i] not in new):
                new.append(nums1[i])
                
        return new    

                
    
if __name__=="__main__":
    s=Solution()
    print(s.intersect([1,2,2,1],[2,2]))