# -*- coding: utf-8 -*-
"""
Created on Sat May  2 18:18:04 2020

@author: abhis
"""

#leetcode 122

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i] - prices[i-1]
        
        return profit
        