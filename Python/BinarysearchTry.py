# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:53:16 2020

@author: abhis
"""

def binarySearch(nums, target):
    
    l = 0
    r = len(nums)
    while(l<r):
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid
    return -1
    
    

print(binarySearch([1,5,7,55,66],5))