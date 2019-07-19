# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 00:26:37 2019

@author: abhis
"""
#leetcode 771

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        c=0
        for i in S:
            for j in J:
                if i==j:
                    c+=1
        return c
                
        
s=Solution()
print(s.numJewelsInStones('ansv','aaAbbs'))