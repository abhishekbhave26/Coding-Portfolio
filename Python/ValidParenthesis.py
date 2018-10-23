# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 00:12:09 2018

@author: abhis
"""
#valid parenthesis 
#leetcode 20

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        list=[]
        if(s[0]==')' or s[0]=='}' or s[0]==']' ):
            return False
        for i in s:
            if(s[i]=='(' or s[i]=='{' or s[i]=='[' ):
                list.append(s[i])
                flag=False
        for i in list:
            pass
        return True
            
s=Solution()
print(s.isValid('[()]'))