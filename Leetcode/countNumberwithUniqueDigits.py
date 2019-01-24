# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:33:34 2019

@author: abhis
"""
#leetcode 357
import math

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if(n==0):
            return 1
        if(n==1):
            return 10;
        if(n==2):
            return 91;
        else:
            q=91;
            for i in range(3,n+1):
                l=9;
                p=9;
                j=i-1;
                for k in range(j):
                    p=p*(l-k);
                    #print(p)
                q=p+q;
            return q;
        

s=Solution()
x=s.countNumbersWithUniqueDigits(3)
print(x)
        