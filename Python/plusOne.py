# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 01:07:34 2018

@author: abhis
"""
#leetocode 66

class Solution:
    def plusOne(self, digits):
        digits=digits[::-1]
        new=[]
        flag=0
        for i in range(0,len(digits)):
            x=digits[i]
            if(i==len(digits)-1):
                if(x==9):
                    while(flag==1):
                        pass
                else:
                    x+=1
                    digits[i]=x
            else:
                new.append(x)
                
        return new[::-1]
    
s=Solution()
print(s.plusOne([1,2,6]))
print(s.plusOne([2,9]))