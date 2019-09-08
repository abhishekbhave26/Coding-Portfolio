# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:26:57 2019

@author: abhis
"""
#leetcode 557
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sList=list(s)
        final=''
        x=''
        for i in sList:
            if(i==' '):
                final+=x[::-1]+' '
                x=''
            else:
                x+=i
        return final+x[::-1]
        
        
s=Solution()
print(s.reverseWords("Let's take LeetCode contest"))