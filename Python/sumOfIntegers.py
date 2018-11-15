# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:00:36 2018

@author: abhis
"""

#leetcode 371
#sum of 2 numbers without using + and -

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        list=[]
        list.append(a)
        list.append(b)
        x=sum(list)
        t=[a,b]
        return sum(t)
        
        return x
    
print(Solution().getSum(5,-3))