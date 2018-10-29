# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:08:04 2018

@author: abhis
"""
#leetocde 507

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum=0
        ncopy=num
        if(ncopy%2!=0):
            ncopy+=1
        #ncopy/=2
        #print(ncopy)
        n=ncopy/2
        for i in range(1,int(n)):
            if(ncopy%i==0):
                sum+=i
                print(i)
        #print(sum)
        if(sum==num):
            return True
        else:
            return False

s=Solution()
print(s.checkPerfectNumber(28))

