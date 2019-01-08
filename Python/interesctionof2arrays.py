# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:04:53 2019

@author: abhis
"""

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d={}
        result=[]
        for i in range(0,len(nums1)):
            if(nums1[i] in d):
                x=d.get(nums1[i])
                x+=1
                d[nums1[i]]=x
            else:
                d[nums1[i]]=1
        for i in range(0,len(nums2)):
            if(nums2[i] in d):
                x=nums2.count(nums2[i])
                y=d.get(nums2[i])
                new=min(x,y)
                copy=new
                while(new>0):
                    result.append(nums2[i])
                    new-=1
                y-=copy
                if(y!=0):
                    d[nums2[i]]=y
                else:
                    d.pop(nums2[i])
                
        return result
                
                    
    
if __name__=="__main__":
    s=Solution()
    print(s.intersect([1,2,2,1],[2,2]))