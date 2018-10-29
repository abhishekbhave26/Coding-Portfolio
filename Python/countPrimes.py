# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:42:33 2018

@author: abhis
"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        '''
        if(n==2):
            return 1
        count=1
        '''
        x=True
        for i in range(2, n):
            if n%i == 0:
                x =False
                break
            else:
                count+=1
        
        return count

s=Solution()
print(s.countPrimes(10))