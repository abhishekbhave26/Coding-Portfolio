# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:30:18 2019

@author: abhis
"""
#leetcode 125

class Solution(object):
    
    
    
    
    
    #works for 554/576 testcases
    #passes all
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        if(len(s)==0):
            return True
        while(l<r):
            
            while l < r and not s[l].isalnum():
                l += 1
            
            while l < r and not s[r].isalnum():
                r-=1
            
                
            if(s[l].lower()!=s[r].lower()):
                return False
            l+=1
            r-=1
        
        return True
    
s=Solution()
x=s.isPalindrome('0P')
print(x)
                
        