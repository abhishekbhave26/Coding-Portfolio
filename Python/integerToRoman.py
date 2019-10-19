# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:31:12 2019

@author: abhis
"""

#leetcode 12

class Solution:
    def intToRoman(self, num: int) -> str:
        res=''
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL',10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        for i in d:
            while(num>=i):
                res += d[i]
                num -= i
        return res
        