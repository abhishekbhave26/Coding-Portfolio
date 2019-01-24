# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 01:26:37 2019

@author: abhis
"""
#leetcode 232

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        x=self.s[0]
        self.s=self.s[1:]
        return x
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.s[0]
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.s)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(3)
obj.push(9)
param_2 = obj.pop()
print(param_2)
param_3 = obj.peek()
param_4 = obj.empty()