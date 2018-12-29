# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 18:19:31 2018

@author: abhis
"""
#leetcode70

class Solution:
    
    def climb(self,i,n,m):
        if(i>n):
            return 0
        if(n==i):
            return 1
        #print(i)
        if (m[i] > 0):
            return m[i]
        
        x=int(Solution.climb(Solution,i+1,n,m)+Solution.climb(Solution,i+2,n,m))
        m.insert(i,x)
        #print('Done')
        return m[i]
        
    def climbStairs(self, n):
        memo=[-1]*(n+1)
        return Solution.climb(Solution,0,n,memo)
    
    def dp(self,n):
        memo=[-1]*(n)
        memo.insert(1,1)
        memo.insert(2,2)
        for i in range(3,n+1):
            x=memo[i-1]+memo[i-2]
            memo.insert(i,x)
        return memo[n]
        
    
        
        
if __name__=="__main__":
    s=Solution()
    x=s.climbStairs(4)
    print(x)
    y=s.dp(4)
    print(y)