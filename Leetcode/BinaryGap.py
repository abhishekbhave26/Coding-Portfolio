# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:57:56 2019

@author: abhis
"""
#leetcode 868

class Solution(object):
    
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        x=bin(N)
        x=x[2:]
        count=0
        stack=[]
        
        for i in range(0,len(x)):
            #print(x[i])
            if(x[i]=='1'):
                stack.append(i)
        if(len(stack)<=1):
            return 0
        
        
        for i in range(0,len(stack)-1):
            a=stack[i+1]-stack[i]
            if(a>count):
                count=a
        return count
        
        
if __name__=="__main__":
    s=Solution()
    x=s.binaryGap(8)
    print(x)
        
        