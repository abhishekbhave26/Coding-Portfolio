# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:09:14 2019

@author: abhis
"""
#leetcode 225

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s=[]
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        x=self.s[len(self.s)-1]
        self.s=self.s[0:len(self.s)-1]
        return x
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        x=len(self.s)
        return self.s[x-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if(len(self.s)==0):
            return True
        else:
            return False
        
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(6)
obj.push(8)
param_2 = obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()