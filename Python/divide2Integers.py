# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:18:54 2019

@author: abhis
"""
#leetcode 29
import math

class Solution(object):
    
    def divide(self, dividend, divisor):     
        neg=( (dividend < 0) != (divisor < 0) )
        dividend = left = abs(dividend)
        divisor  = div  = abs(divisor)
        Q = 1
        ans = 0
        while left >= divisor:
            left -= div
            ans  += Q 
            Q    += Q
            div  += div
            if left < div:
                div = divisor
                Q = 1
        if neg:
            return max(-ans, -2147483648)
        else:
            return min(ans, 2147483647)
    
    
    
    
    def divide2(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        q=0
        dend,div=dividend,divisor
        while(dividend>=divisor):
            if(divisor<0):
                divisor=abs(divisor)
            dividend-=divisor
            q+=1
    
        qcopy=q
        if(dend<0 and div>0):
            q=-q
        if(dend>0 and div<0):
            q=-q
        if(dend<0 and div<0):
            q=qcopy
        
        return q
        
s=Solution()
x=s.divide(1,1)
print(x)