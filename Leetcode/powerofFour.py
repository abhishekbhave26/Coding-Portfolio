# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:51:22 2019

@author: abhis
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while(n%4==0):
            n/=4
        return n==1
            
        


class Solution2():
    def isPowerOfFour(self,num):
    	# check non-positive
    	if num <= 0:
    		return False
    		
    	# check whether num is a sequence of zeros with only one leading one
    	# this step sift out the power of 2
    	if num & (num-1):
    		return False
    		
    	# create a mask that sift out the odd position bit
    	mask = 0x55555555
    	# if something remains, then it is power of 4
    	if num & mask == num:
    		return True
    	return False
    
s=Solution()
print(s.isPowerOfFour(100))