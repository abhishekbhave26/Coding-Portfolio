# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 20:23:20 2018

@author: abhis
"""

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
    
        x=len(s)
        y=len(t)
        tmp=t
        
        '''
        for i in range(x):
            
            count=0
            for j in range(y):
                count+=1
                if(s[i]==t[j]):
                    #count+=1
                    tmp=tmp.replace(t[j],'') 
                    if(x==1 or x==2 and t[0]==s[0]):
                        tmp+=(t[0])
                        return tmp
                
        return tmp
        '''
        sums=0
        sumt=0
        for i in range(x):
            sums+=int(ord(s[i]))
        
        for j in range(y):
            sumt+=int(ord(t[j]))
            
        sums=sumt-sums
        return chr(sums)

s=Solution()
print(s.findTheDifference('ae','aea'))