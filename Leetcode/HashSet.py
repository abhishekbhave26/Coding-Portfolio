# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:59:35 2019

@author: abhis
"""

#leetcode 705

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d={}

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.d[key]=1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if(key in self.d):
            del self.d[key]
        
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if(key in self.d):
            return True
        else:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)