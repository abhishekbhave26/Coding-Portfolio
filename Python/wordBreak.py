# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 00:03:59 2019

@author: abhis
"""
#leetcode 139

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #dp solution, passes all test cases
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the             wordDicts 
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]
        
    #my solution passes 32/36 test cases
    def wordBreak2(self, s, wordDict):
        dic={}
        for i in wordDict:
            dic[i]=1
        x=''
        for i in s:
            x+=i
            if(x in dic):
                x=''
        if(len(x)!=0):
            return False
        else:
            return True
        
s=Solution()
print(s.wordBreak('aaaaaaa',['aaaa','aaa']))
print(s.wordBreak('a',['']))
        