# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:20:18 2019

@author: abhis
"""
#leetcode 67

import math

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum1,sum2=0,0
        for i in range(0,len(a)):
            x=int(a[len(a)-i-1])
            new=int(x*math.pow(2,i))
            sum1+=new
        for i in range(0,len(b)):
            x=int(b[len(b)-i-1])
            new=int(x*math.pow(2,i))
            sum2+=new
        x=bin(sum1+sum2)
        return x[2:]
    
    def addBinary2(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]
        
        
if __name__=="__main__":
    s=Solution()
    x=s.addBinary2('11','1')
    print(x)