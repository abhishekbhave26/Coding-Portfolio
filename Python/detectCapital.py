# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 19:47:57 2019

@author: abhis
"""

#leetcode 520

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        x=[]
        for i in range(0,len(word)):
            if(word[i].isupper()):
                x.append(1)
            else:
                x.append(0)
        if(len(set(x))==1):
            return True
        elif(len(set(x[1:]))==1 and x[0]==1):
            return True
        else:
            return False
        
                
            
                
        