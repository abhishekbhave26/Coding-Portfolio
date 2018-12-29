# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:08:48 2018

@author: abhis
"""

#leetcode 119

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if(rowIndex==0):
            return []
        if(rowIndex==1):
            return [[1]]
        new=[]*(rowIndex)
        new.append([1])
        new.append([1,1])
        for i in range(2,rowIndex+1):
            c=[]
            c.append(1)
            for j in range(1,i):
                x=new[i-1][j-1]+new[i-1][j]
                c.append(x)
                
                #print('thisvvv')
            c.append(1)
            new.append(c)
            
        return new[rowIndex]
        
        
        
        

if __name__=="__main__":
    s=Solution()
    x=s.getRow(4)
    print(x)