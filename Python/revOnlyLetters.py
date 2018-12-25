# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:33:59 2018

@author: abhis
"""
#leetcode 917

class Solution:
    def reverseOnlyLetters2(self, S):
        """
        :type S: str
        :rtype: str
        """
        x=len(S)
        l=[]
        for i in range(0,x):
            a=ord(S[i])
            if(a>=65 and a<=122):
                l.append(S[i])
        print(l)
        res = ""
        for i, s in enumerate(S):
            a=ord(s)
            if(a>=65 and a<=122):
                res += l.pop()
            else:
                res += s
        return res

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        letters = []
        N = len(S)
        for i, s in enumerate(S):
            if s.isalpha():
                letters.append(s)
        print(letters)
        res = ""
        for i, s in enumerate(S):
            if s.isalpha():
                res += letters.pop()
                print(res)
            else:
                res += s
        return res

                      
            
    
s=Solution()
x=s.reverseOnlyLetters('a-bC-dEf-ghIj')
print(x)