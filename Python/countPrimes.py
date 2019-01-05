# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:42:33 2018

@author: abhis
"""

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=[]
        if(n>2):
            count.append(2)
        i=3
        while(i<n):
            x=Solution.isPrime(Solution,i)
            if(x):
                count.append(i)
            i+=2
        print(count)
        return len(count)
        
    def isPrime(self,number):
        for i in range(2,int(number/2)):
            if(number%i==0):
                return False
        return True

class Solution2():        
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 0
        
        nums = [None] * n
        nums[0] = False
        nums[1] = False
        
        for i in range(n):
            if nums[i] == None:
                nums[i] = True
                
                # set all multiples of i to False
                for j in range(i+i, n, i):
                    nums[j] = False
        
        return sum(nums)
        
        
     
s=Solution2()
print(s.countPrimes(3))