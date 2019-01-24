# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 01:26:39 2019

@author: abhis
"""
#leetcode 509

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a=0
        b=1
        for i in range(N):
            x=a+b
            a=b
            b=x
        return a

if __name__=="__main__":
    s=Solution()
    x=s.fib(5)
    print(x)
    
