# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 14:31:13 2019

@author: abhis
"""
#leetcode 633
import math

class Solution:
    #time limit exceeded
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        d={}
        i=0
        while(i*i<=c):
            d[i*i]=i
            i=+1
        for i in d:
            if((c-i) in d):
                return True
        return False
    
    def judgeSquareSum2(self,c):
        i=0
        while(i*i<=c):
            x=(math.sqrt(c-(i*i)))
            if(x==int(x)):
                return True
            else:
                i+=1
        return False
    
if __name__=="__main__":
    s=Solution()
    print(s.judgeSquareSum2(1000000000))