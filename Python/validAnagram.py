# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:51:51 2019

@author: abhis
"""
#leetcode 242

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d={}
        if(len(s)!=len(t)):
            return False
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in t:
            if i in d and d[i]>0:
                d[i]-=1
            else:
                return False
                
        return True
        


s=Solution()
x=s.isAnagram('ab','a')
print(x)
        
        
        
        