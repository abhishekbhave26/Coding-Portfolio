# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:22:38 2019

@author: abhis
"""
#leetcode 50

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1/self.myPow(x,-n)
        elif n % 2 == 0:
            y = self.myPow(x,n//2)
            return y*y
        else:
            y = self.myPow(x,(n-1)//2)
            return x*y*y
        