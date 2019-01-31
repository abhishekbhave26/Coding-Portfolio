# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 23:54:18 2019

@author: abhis
"""
#leetcode 824

class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res=''
        
        def word(i,n):
            new=''
            s=i[0].lower()
            if(s in ['a','e','i','o','u']):
                i+='ma'
                y=i
            else:
                x,y=i[0],i[1:]
                y+=x+'ma'
            
            y+=(str('a')*(n))
            new+=y
            
            return new
        x=0
        a=S.split()
        for i in range(0,len(a)):
            res+=word(a[i],x+1)
            if(i!=len(a)-1):
                res+=' '
            x+=1
        return res
    
s=Solution()
x=s.toGoatLatin("I speak Goat Latin")
print(x)