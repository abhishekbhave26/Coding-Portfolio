# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 00:51:03 2019

@author: abhis
"""

#leetcode 380

import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if(val not in self.dic):
            self.dic[val]=1
            return True
        return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if(val in self.dic):
            del self.dic[val]
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        x=self.dic.keys()
        return random.choice(x)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()