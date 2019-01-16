# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:41:55 2019

@author: abhis
"""
#leetcode 720

class Solution:
    
    
    
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        print(wordset)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(1, len(word))):
                    ans = word
    
        return ans
    
    
    
    
    def longestWord2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        d={}
        for i in words:
            if(i in d):
                d[i]+=1
            else:
                d[i]=1
        flag=True
        new=[]
        while(flag):
            x=(max(words))
            result=x[0]
            for i in range(1,len(x)):
                result+=x[i:i+1]
                print(result)
                if(result not in d):
                    words.remove(x)
                    break
                if(result==x):
                    new.append(x)
                    words.remove(x)
                    break
                if(len(words)==0):
                        flag=False
        print(new)
        for n in new:
            print(n)
            #print(chr(n))
        return True

if __name__=="__main__":
    s=Solution()
    x=s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
    print(x)