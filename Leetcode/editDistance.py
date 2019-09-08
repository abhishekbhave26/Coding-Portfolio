# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 11:29:18 2019

@author: abhis
"""

class Solution(object):
    def minDistance(self, s1, s2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n=len(s1),len(s2)
        dp = [[0 for x in range(n+1)] for x in range(m+1)]
        for i in range(0,m+1):
            for j in range(0,n+1):
                if(i==0):
                    dp[i][j]=j
                elif(j==0):
                    dp[i][j]=i
                elif(s1[i-1]==s2[j-1]):
                    dp[i][j]=dp[i-1][j-1]
                else:
                    temp=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                    dp[i][j]=temp+1
        return dp[i][j]
                
s=Solution()
print(s.minDistance('horse','ros'))