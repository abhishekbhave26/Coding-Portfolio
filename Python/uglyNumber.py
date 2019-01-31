# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 18:07:19 2019

@author: abhis
"""

#leetcode 263

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while num % x == 0:
                num = num / x
        return num == 1
    
s=Solution()
x=s.isUgly(7)
print(x)