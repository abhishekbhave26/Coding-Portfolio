# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 23:59:50 2019

@author: abhis
"""
#leetcode 179

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num