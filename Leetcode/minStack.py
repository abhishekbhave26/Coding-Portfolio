# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:47:25 2019

@author: abhis
"""
#leetcode 155

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s=[]        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        
        self.s.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        x=len(self.s)
        return self.s[x-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.s)
        


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(7)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()