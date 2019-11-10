# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:44:02 2019

@author: abhis
"""

#leetcode 9

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x%10==0 and x!=0)):
            return False
        number=0
        while(x>number):
            number = number * 10 + x % 10;
            x=int(x/10)
        print(x,int(number/10))
        return x == number or x == int(number/10)
            
            
            
x=Solution.isPalindrome(Solution,121)
print(x)