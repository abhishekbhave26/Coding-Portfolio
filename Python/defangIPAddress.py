# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 00:18:58 2019

@author: abhis
"""
#leetcode 1108

class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=address.replace('.','[.]')
        return s
    
s=Solution()
print(s.defangIPaddr('23.56.32.5'))
        