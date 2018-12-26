# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 20:15:03 2018

@author: abhis
"""

#nim game
#leetcode 292

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return(n%4!=0)
    
s=Solution()
x=s.canWinNim(5)
print(x)