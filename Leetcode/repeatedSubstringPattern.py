# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:44:06 2019

@author: abhis
"""
#leetcode 459

class Solution:
    def repeatedSubstringPattern(Solution,s):
        
        newstr = s[1:] + s[:-1]
        print(newstr)
        return newstr.find(s) != -1
    
s=Solution()
x=s.repeatedSubstringPattern('abab')
print(x)
    
            
            
        