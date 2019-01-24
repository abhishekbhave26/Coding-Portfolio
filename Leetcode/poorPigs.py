# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 23:23:50 2019

@author: abhis
"""
#leetcode 458

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
        