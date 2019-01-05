# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:07:02 2019

@author: abhis
"""

#leetcode 441

class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=0
        if(n<=0):
            return 0
        if(n==1):
            return 1
        sum=n
        for i in range(1,n+1):
            sum-=i
            if(sum<0):
                return i-1
                
if __name__=="__main__":
    s=Solution()
    print(s.arrangeCoins(5))