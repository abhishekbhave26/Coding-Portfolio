# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 00:41:20 2018

@author: abhis
"""
#leetcode 338

class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result=[]
        for i in range(0,num+1):
            x=bin(i)
            x=x[2:]
            x=str(x)
            #print(x)
            new=x.count('1')
            result.append(new)
        return result



if __name__=="__main__":
    s=Solution()
    x=s.countBits(10)
    print(x)