# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:21:14 2019

@author: abhis
"""

#leetcode 434

class Solution:
    def countSegments(self, s: str) -> int:
        x=s.split()
        return len(x)
        
x=Solution.countSegments(Solution,'This is a cra')
print(x)