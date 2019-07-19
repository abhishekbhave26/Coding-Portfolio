# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:01:40 2019

@author: abhis
"""

#leetcode 13

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        z=0
        d={'I':1,'V' :5,'X':10,'L' :50,'C' :100,'D':500,'M':1000 }
        #print(s[-1])
        for i in range(0, len(s) - 1):
            if d[s[i]] < d[s[i+1]]:
                z -= d[s[i]]
            else:
                z += d[s[i]]
        return z + d[s[-1]]
        
    
        
s=Solution()
x=s.romanToInt("IX")
print(x)