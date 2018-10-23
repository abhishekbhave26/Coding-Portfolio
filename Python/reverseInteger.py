# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 23:34:38 2018

@author: abhis
"""
#leetocde 7

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x>1534236468 or x<-2147483648):
            return 0
        temp=str(x)
        n=len(temp)
        
        if(temp[0]=='-'):
            if(temp[n-1]=='0'):
                s=temp[::-1]
            
                temp=temp[0]+s[:len(s)-1]
            else:
                s=temp[::-1]
                temp=temp[0]+s[:len(s)-1]
        
        else:
            if(temp[n-1]=='0'):
                temp=temp[::-1]
            else:
                temp=temp[::-1] 
        x=int(temp)
        return x
            
s=Solution()
print(s.reverse(-901000))
            