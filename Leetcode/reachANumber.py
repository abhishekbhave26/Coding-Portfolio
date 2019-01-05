# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 22:05:41 2019

@author: abhis
"""
#leetcode 754 

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        return k if target % 2 == 0 else k + 1 + k%2
        

if __name__=="__main__":
    s=Solution()
    print(s.reachNumber(5))
        