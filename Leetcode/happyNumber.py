# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 19:06:30 2019

@author: abhis
"""
#leetcode 202

class Solution:
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        d={}
        
        return Solution.helper(Solution,n,d)
    
    def helper(self,n,d):
        i,copy=0,0
        while(n>=1):
            i=n%10
            #print(i)
            copy+=i*i
            n=int(n/10)
        
        if(copy==1):
            return True
        else:
            if(copy in d.keys()):
                return False
            else:
                d[copy]=1
                
        return Solution.helper(Solution,copy,d)
    
    
            
s=Solution()
x=s.isHappy(19)
print(x)
                
                
            