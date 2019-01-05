# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 18:08:12 2018

@author: abhis
"""

import unittest
    
class Solution():
    def fun(x):
        return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.fun(3), 4)
    
        
        
s=MyTest()   
s.test()