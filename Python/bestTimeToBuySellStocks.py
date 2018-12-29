# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 00:12:43 2018

@author: abhis
"""
#leetcode 121

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        new=[]
        maxProfit=0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                x=prices[j]-prices[i]
                if(x>maxProfit):
                    maxProfit=x
            new.append(maxProfit)
        if(len(new)==0):
            return 0
        return max(new)
 
    
    def maxProfit2(self,prices):
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            print(min_price)
            profit = price - min_price
            print(profit)
            max_profit = max(max_profit, profit)
            print(max_profit)
        return max_profit
            
        
                

if __name__=="__main__":
    s=Solution()
    x=s.maxProfit2([7,1,4,3,1])
    print(x)