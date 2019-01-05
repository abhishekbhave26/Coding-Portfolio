# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:19:19 2019

@author: abhis
"""

import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        s=calc.Solution()
        self.assertEqual(s.add(10,5),15)
        self.assertEqual(s.add(-1,1),0)
        self.assertEqual(s.add(-1,-76),-77)
        
    def test_subtract(self):
        s=calc.Solution()
        self.assertEqual(s.subtract(10,5),5)
        self.assertEqual(s.subtract(-1,1),-2)
        self.assertEqual(s.subtract(1,-76),77)
        
    def test_multiply(self):
        s=calc.Solution()
        self.assertEqual(s.multiply(10,0),0)
        self.assertEqual(s.multiply(-1,1),-1)
        self.assertEqual(s.multiply(-1,-76),76)
        
    def test_divide(self):
        s=calc.Solution()
        self.assertEqual(s.divide(10,9),10/9)
        self.assertEqual(s.divide(-1,1),-1)
        self.assertEqual(s.divide(-76,-1),76)
        self.assertEqual(s.divide(-1,-2),0.5)
        
        with self.assertRaises(ValueError):
            s.divide(10,0)
        
if __name__=="__main__":
    unittest.main()