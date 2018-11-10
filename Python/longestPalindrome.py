# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:24:44 2018

@author: abhis
"""

def longest_palindrome(a):
    x=len(a)
    acopy=a
    a=a.lower()
    for l,start,end in substrings(a):
        if palindrome(l):
            return (acopy[start:end])
    
    
def palindrome(s):
    return s == s[::-1]

def substrings(s):
    l = len(s)
    for end in range(l, 0, -1):
        for i in range(l-end+1):
            yield s[i: i+end],i,end+i

 
print(longest_palindrome('my gym'))
                            #Ab1ba