# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:33:34 2018

@author: abhis
"""

def maxOccurences(totalHrs,maxHours,nums):
    remdays=0
    remhrs=0
    c=0
    for i in nums:
        if(i=='?'):
            remdays+=1
        else:
            a=int(nums[c])
            totalHrs=totalHrs-a
            remhrs=totalHrs
        c+=1
    return remdays,remhrs
        
        
nums='???8???'
x,y=maxOccurences(56,8,nums)
print('Remaining days is {}'.format(x))
print('Remaining hours is {}'.format(y))
