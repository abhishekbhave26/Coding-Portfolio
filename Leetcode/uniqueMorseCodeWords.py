# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 18:18:32 2019

@author: abhis
"""
#leetcode 804

class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        a=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        a = { i+97 : a[i] for i in range(0, len(a) ) }
        new={}
        for i in words:
            temp=''
            for j in i:
                j=ord(j)
                temp+=a[j]
            if temp in new:
                new[temp]+=1
            else:
                new[temp]=1
        return len(new)
 

       
s=Solution()
words = ["gin", "zen", "gig", "msg"]
x=s.uniqueMorseRepresentations(words)
print(x)