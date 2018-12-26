# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:41:43 2018

@author: abhis
"""

#lettcode 387

class Solution():
    def firstUniqChar(self,s):
        if(s==''):
            return -1
        d={}
        l=[]
        flag=True
        for i in range(0,len(s)):
            if(flag):
                l.append(s[i])
            if(s[i] in d and flag==False): 
                #print(s[i])
                l.remove(s[i])
                flag=False
                x=d.get(s[i])
                x+=1
                d[s[i]]=x
            else:
                d[s[i]]=1
        if(len(l)==1):
            x=l[0]
        else:
            return -1
        for i in range(0,len(s)):
            if(s[i]==x):
                return i
s=Solution()
print(s.firstUniqChar('loveleetcode'))