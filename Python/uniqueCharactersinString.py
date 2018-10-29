# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 21:41:43 2018

@author: abhis
"""

#lettcode 387

    
s='cc'
for i in range(0,len(s)-1):
    if(s[i] in s[i+1:]):
        #print(s[i+1:])
        pass
    else:
        print(i)
        print(s[i])
        break

#s=Solution()
#print(s.firstUniqChar('leetcode'))