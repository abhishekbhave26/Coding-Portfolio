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
        
    def checkPerfectNumber2(self, num):
         
        sum=0
        ncopy=num
        if(ncopy%2==0):
            mid=ncopy/2
            sum+=1
            x=1
        else:
            mid=int((ncopy/2)+0.5)
            sum+=1
            x=2

            
        mid=int(mid)   
        for i in range(2,mid+1,x):
            if(ncopy%i==0):
                sum+=i
                print(i)
        
        if(sum==num):
            return True
        else:
            return False

s=Solution()
print(s.checkPerfectNumber2(28))



