# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:51:17 2019

@author: abhis
"""
#leetcode 844

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #S = list(S)
        #T = list(T)
        l = []
        l2 = []
        for i in range(len(S)):
            if S[i] != "#":
                l.append(S[i])
            else:
                if l == []:
                    i+=1
                else:
                    l.pop()
        
        for i in range(len(T)):
            if T[i] != "#":
                l2.append(T[i])
            else:
                if l2 == []:
                    i+=1
                else:
                    l2.pop()
        return "".join(l) == "".join(l2)