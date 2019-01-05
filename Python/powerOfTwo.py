# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:23:25 2019

@author: abhis
"""
#leetcode 231

import math

class Solution2:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and n&(n-1) == 0

        if(n!=1 and n%2==1):
            return False
        for i in range(0,int(math.sqrt(n))):
            if(n==math.pow(2,i)):
                return True
        return False
        
class Solution():
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n==1:
            return True
        length = len(bin(n))-2
        if 1<<(length-1) == n:
            return True
        else:
            return False
        
if __name__=="__main__":
    s=Solution()
    print(s.isPowerOfTwo(2147483646))
    print(s.isPowerOfTwo(15649))