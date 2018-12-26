# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:51:23 2018

@author: abhis
"""
import operator

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        s=paragraph.lower()
        new=''
        punc=[',','.','!',';']
        for i in s:
            if(i in punc):
                s.replace(i,' ')
                new=new+' ' 
            else:
                new=new+i
        print(s)
        s=new.split()
        d={}
        for i in s:
            if(i in d):
                x=d.get(i)
                x+=1
                d[i]=x
            else:
                d[i]=1
        flag=True
        
        while(flag):
        
            s=max(d.items(), key=operator.itemgetter(1))[0]
            print(d)
            print(s)
            if(s in banned):
                
                d.pop(s)
                flag=True
    
            else:
                flag=False
                return s
            
                
s=Solution()
x=s.mostCommonWord('a, a, a, a, b,b,b,c, c','a')
print(x)