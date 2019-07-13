# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 23:34:38 2018

@author: abhis
"""
#leetocde 7

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x>1534236468 or x<-2147483648):
            return 0
        temp=str(x)
        n=len(temp)
        
        if(temp[0]=='-'):
            if(temp[n-1]=='0'):
                s=temp[::-1]
            
                temp=temp[0]+s[:len(s)-1]
            else:
                s=temp[::-1]
                temp=temp[0]+s[:len(s)-1]
        
        else:
            if(temp[n-1]=='0'):
                temp=temp[::-1]
            else:
                temp=temp[::-1] 
        x=int(temp)
        return x
    
    #my latest code
    def reverse2(self, x):
        new=str(x)
        res=''
        rev=''
        for i in range(0,len(new)):
            if new[i].isnumeric:
                rev+=new[i]
            else:
                res+=new[i]
                rev=rev*-1
        res+=rev[::-1]
        final=''
        l=len(res)
        if(res[l-1]=='-'):
            final=res[0:l-1]
            final=int(final)
            if(-1*final<pow(-2,31)):
                return 0
            else:
                return -1*final
        else:
            if(int(res)>pow(2,31)-1):
                return 0
            else:
                return int(res)
    
                 
            
s=Solution()
print(s.reverse2(120))
            