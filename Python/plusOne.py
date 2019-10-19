# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 02:23:32 2019

@author: abhis
"""

#leetcode 66

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        g=''
        for i in digits:
            g+=str(i)
        x=int(g)
        x+=1
        y=str(x)
        return [g for g in y]
