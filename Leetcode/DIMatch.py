# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 00:48:05 2019

@author: abhis
"""
#leetcode 942

class Solution:
    def diStringMatch(self, S):
        
        lo,hi=0,len(S)
        res=[]
        for i in range(0,len(S)): 
            if(S[i]=='I'):
                res.append(lo)
                lo+=1
            else:
                res.append(hi)
                hi-=1
            print(res)
        res.append(lo)
        return res
    
s=Solution()
print(s.diStringMatch("DDI"))