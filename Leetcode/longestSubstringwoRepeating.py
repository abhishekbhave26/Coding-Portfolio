# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:17:05 2019

@author: abhis
"""
#leetcode 3
#length of longest non repeating substring

class Solution:
    #my code n^2 complexity
    def lengthOfLongestSubstring(self,s):
        res=''
        final={}
        if(len(s)==0):
            return 0
        if(len(s)==1):
            return 1
        for i in range(0,len(s)):
            dict={}
            dict[s[i]]=1
            res+=s[i]
            for j in range(i+1,len(s)):
                if s[j] not in dict:
                    dict[s[j]]=1
                    res+=s[j]
                else:
                    break
            final[res]=len(res)
            res=''
        x=max(final, key=final.get)
        print(final)
        return final[x]
    
    def lengthOfLongestSubstring2(self,s):
        #n complexity
        if s == "":
            return 0
        max_len = 0
        dic = {}
        temp = ""
        for letter in s:
            if letter not in temp:
                temp+=letter
                if len(temp)>=max_len:
                    max_len = len(temp)
                    dic[max_len] = temp

            elif letter in temp:
                temp = temp[temp.index(letter)+1:] + letter
        keylist = dic.keys()
        f=(sorted(keylist))
        return f[-1]
    
# sliding window solns
class Solution2(object):
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ans = i = j = 0
        while(i<len(s) and j<len(s)):
            if s[j] not in dic:
                dic[s[j]]=1
                j+=1
                ans = max(ans,j-i)
            else:
                del dic[s[i]]
                i+=1
        return ans
    
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        ans = i = j = 0
        while(i<len(s) and j<len(s)):
            if s[j] in dic:
                i = max(dic[s[j]],i)
            ans = max(ans, j-i+1)
            dic[s[j]]= j+1
            j+=1
        return ans
                
        
s=Solution()
result=s.lengthOfLongestSubstring2('abczbcbb')
print((result))
