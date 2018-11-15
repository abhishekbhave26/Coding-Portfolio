# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:43:26 2018

@author: abhis
"""
#leetcode 345

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list=['a','e','i','o','u']
        latest=[]
        for i in range(0,len(s)):
            if(s[i] in list):
                latest.append(s[i])
        
        #print(latest)
        
        j=len(latest)-1
        res=''
        for i in s:
            if(i in list):
                res+=latest[j]
                j-=1
            else:
                res+=i
        
            
        return res
        
        
s=Solution()
x=s.reverseVowels('hello world')
print(x)