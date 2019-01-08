# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 12:36:52 2019

@author: abhis
"""

#leetcode 168

class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        d={}
        x=65
        for i in range(1,27):
            y=chr(x)
            d[i]=y
            x+=1
        if(n>26):
            
            
        else:
            return d[n]
            
        
        
        
if __name__=="__main__":
    s=Solution()
    x=s.convertToTitle(26)
    print(x)