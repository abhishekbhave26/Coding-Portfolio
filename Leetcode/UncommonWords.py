# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 02:56:58 2019

@author: abhis
"""
#leetcode 884

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a={}
        new=[]
        A,B=A.split(),B.split()
        #print(A)
        for i in A:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        #print(a)
        for i in B:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        
        x=(list(a.keys()))
        for i in x:
            d=a[i]
            if(d==1):
                new.append(i)
        return new
                
            
        
        
s=Solution()
print(s.uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour"))