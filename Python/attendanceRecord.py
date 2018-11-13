# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 21:57:02 2018

@author: abhis
"""
#leetcode 551
#attendance record

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count=0
        flag=0
        for i in range(0,len(s)):
            if(s[i]=='A'):
                count+=1
        if(count>1):
            return False
        
        for i in range(0,len(s)-2):
            if(s[i]=='L'):
                flag=1
            if(s[i]==s[i+1]==s[i+2]=='L' and flag==1):
                #print(i)
                return False
        return True

s=Solution()
x=s.checkRecord('LALL')
print(x)