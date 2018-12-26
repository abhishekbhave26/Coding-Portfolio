# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:15:03 2018

@author: abhis
"""

#leetcode 374

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        j=n
        
        while(i<=j):
            mid=(i+j)/2  
            x=guess(mid)
            if(x==0):
                return mid 
            elif(x==-1):
                j=mid-1
            else:
                i=mid+1
        return -1
 