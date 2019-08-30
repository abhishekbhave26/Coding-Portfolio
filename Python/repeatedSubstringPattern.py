# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:44:06 2019

@author: abhis
"""
#leetcode 459

class Solution:
    def repeatedSubstringPattern2(Solution,s):
        
        newstr = s[1:] + s[:-1]
        print(newstr)
        return newstr.find(s) != -1
    
    def repeatedSubstringPattern(self, s: str) -> bool:
        s1=s+s
        s2=s1[1:-1]
        if(s in s2):
            return True
        else:
            return False
        
    
s=Solution()
x=s.repeatedSubstringPattern('abab')
print(x)
    
            
            
        