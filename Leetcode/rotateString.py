# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 02:25:12 2018

@author: abhis
"""
#leetcode 796

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        new=[]
        for i in range(0,len(A)+1):
            x=A[0:i]
            y=A[i:]
            string=y+x
            new.append(string)
        if(B in new):
            return True
        else:
            return False
        
        
        
s=Solution()
print(s.rotateString('abcde','cdeab'))