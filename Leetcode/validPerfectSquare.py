# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 18:51:19 2019

@author: abhis
"""

#leetcode 367

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        lo=0
        hi=num
        while lo<=hi:
            mid=(lo+hi)//2
            sqr=mid*mid
            if sqr<num:
                lo=mid+1
            elif sqr>num:
                hi=mid-1
            else:
                return True
        return False

    
            
s=Solution()
x=s.isPerfectSquare(16)
print(x)