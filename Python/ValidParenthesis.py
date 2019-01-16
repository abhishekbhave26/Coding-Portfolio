# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 00:12:09 2018

@author: abhis
"""
#valid parenthesis 
#leetcode 20

class Solution(object):
    def isValid(self, s):
        
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
    
    
        
        
        
        
            
s=Solution()
print(s.isValid('[()]'))