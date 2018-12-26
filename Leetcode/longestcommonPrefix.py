# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 00:27:40 2018

@author: abhis
"""

class Solution:
    def longestCommonPrefix(self, strs):
       
        new=[]
        v=0
        x=min(strs)
        length=len(x)
        #print(length)
        for j in range(0,length):
            list=[]
            for i,v in enumerate(strs):
                s=strs[i][j]
                
                list.append(s)
            print(list) 
            
            for i in range(len(list)-1):
                if(list[i]==list[i+1]):
                    pass
                else:
                    return ""
                
            new.append(list[i])
        s=''
        print(new)
        for i in new:
            s+=new[i]
        return s 

s=Solution()
a=['dagaa','dagaa','dagaa','daga']
print(s.longestCommonPrefix(a))
        