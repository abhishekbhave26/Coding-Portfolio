# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 21:44:50 2018

@author: abhis
"""

#leetcode 739 
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        new=[]
        for i in range(0,len(T)):
            for j in range(i,len(T)):
                flag=True
                if(T[j]>T[i]):
                    new.append(j-i)
                    flag=False
                    break
                else:
                    pass
            if(flag):
                new.append(0)     
        return new
        
s=Solution()
x=s.dailyTemperatures([73,74,75,71,69,72,76,73])
print(x)