# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:01:00 2019

@author: abhis
"""
#leetcode 1200

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        curr_max=999999999
        arr.sort()
        res=[]
        for i in range(0,len(arr)-1): 
            x=abs(arr[i]-arr[i+1])
            if(x<curr_max):
                curr_max=x
                res=[[arr[i],arr[i+1]]]
            elif(x==curr_max):
                res.append([arr[i],arr[i+1]])
        return res
    
            
          
            