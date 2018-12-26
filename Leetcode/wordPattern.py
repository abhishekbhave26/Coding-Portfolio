# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 21:40:00 2018

@author: abhis
"""
#leetcode 290

class Solution(object):
    def wordPattern(self, pattern, str):
        d={}
        x=str.split(' ')
        if(len(x)==1):
            x=''.join(x)
        if(x==pattern and x[0]==pattern[0]): return False
        if(len(pattern)==1 and x[0]==pattern): return True
        if(len(x) != len(pattern) and pattern in x): return False
        
        
        
        for i in range(0,len(pattern)):
            if(pattern[i] in d or x[i] in d.values()):
                new=d.get(pattern[i])
                if(new!=x[i]):
                    return False
                     
            else:
                d[pattern[i]]=x[i]
              
        return True
        

s=Solution()
print(s.wordPattern("h","afjafdjpawr"))