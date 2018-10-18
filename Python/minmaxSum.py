# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 19:06:26 2018

@author: abhis
"""

def miniMaxSum(arr):
    arr.sort()
    x=len(arr)
    minsum=(arr[0]+arr[1]+arr[2]+arr[3])
    maxsum=arr[x-1]+arr[x-2]+arr[x-3]+arr[x-4]
    print('{} {}'.format(minsum,maxsum))
    
n=[5,2,3,6,4,88,5,6,4,2,5,1,-900]
miniMaxSum(n)