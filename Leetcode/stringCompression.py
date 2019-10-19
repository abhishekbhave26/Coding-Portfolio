# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:15:59 2019

@author: abhis
"""

#leetcode 443

class Solution:
    def compress(self, chars: List[str]) -> int:
        if(len(chars) in [1,0]):
            return len(chars)
        x=chars[0]
        c=1
        j=0
        for i in range(1,len(chars)):
            if(x==chars[i]):
                c+=1
            else:
                x=chars[i]
                if(c==1):
                    chars[j]=chars[i-1]
                    j+=1
                else:
                    chars[j]=chars[i-1]
                    temp=str(c)
                    j+=1
                    n=0
                    while(n<len(temp)):
                        chars[j]=temp[n]
                        j+=1
                        n+=1
                    c=1
        if(c!=1):
            chars[j]=chars[i-1]
            temp=str(c)
            j+=1
            n=0
            while(n<len(temp)):
                chars[j]=temp[n]
                j+=1
                n+=1
        else:
            chars[j]=chars[i]
            j+=1
        print(chars[:j])
        return len(chars[:j])
        