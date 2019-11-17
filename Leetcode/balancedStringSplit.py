# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 13:30:39 2019

@author: abhis
"""

#leetcode 1221

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        lcount=0
        rcount=0   
        for i in range(0,len(s)):
            if(s[i]=='L'):
                lcount+=1
            else:
                rcount+=1
            if(lcount==rcount and lcount!=0):
                count+=1
                lcount,rcount=0,0
        return count