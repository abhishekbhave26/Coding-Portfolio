# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 01:07:34 2018

@author: abhis
"""
#leetocode 66

class Solution:
    def plusOne(self, digits):
        length=len(digits)
        x=digits.pop()
        if(x==9 and length==1):
            digits.append(1)
            digits.append(0)
            return digits
        x+=1
        digits.append(x)
        return digits
    
s=Solution()
print(s.plusOne([9]))