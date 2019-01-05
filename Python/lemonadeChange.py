# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 00:48:48 2019

@author: abhis
"""
#leetcode 860

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if(bills[0]==10 or bills[0]==20):
            return False
        change5=0
        change10=0
        for i in range(0,len(bills)):
    
            if(bills[i]==5):
                change5+=1
            elif(bills[i]==10 and change5>=1):
                change5-=1
                change10+=1
            elif((bills[i]==20 and change10>=1 and change5>=1)):
                    change5-=1
                    change10-=1
            elif(bills[i]==20 and change5>=3):
                change5-=3
                
            else:
                return False
        return True
            

if __name__=="__main__":
    s=Solution()
    x=s.lemonadeChange([5,10])
    print(x)
    
        