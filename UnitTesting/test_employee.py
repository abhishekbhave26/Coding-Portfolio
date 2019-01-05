# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:56:14 2019

@author: abhis
"""

import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setUp')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDown')        
    
    
    def setUp(self):
        self.emp_1=Employee('Abhishek','Bhave',50000)
        self.emp_2=Employee('Rohan','Nayak',60000)
         
    def tearDown(self):
        pass
        
        
    
    def test_email(self):
        
        self.assertEqual(self.emp_1.email,'Abhishek.Bhave@email.com')
        self.assertEqual(self.emp_2.email,'Rohan.Nayak@email.com')
        
        self.emp_1.first='Thomas'
        self.emp_2.first='Omkar'
        
        self.assertEqual(self.emp_1.email,'Thomas.Bhave@email.com')
        self.assertEqual(self.emp_2.email,'Omkar.Nayak@email.com')
        
    def test_fullname(self):
               
        self.assertEqual(self.emp_1.fullname,'Abhishek Bhave')
        self.assertEqual(self.emp_2.fullname,'Rohan Nayak')
        
        self.emp_1.last='Doe'
        self.emp_2.last='Nair'
        
        self.assertEqual(self.emp_1.fullname,'Abhishek Doe')
        self.assertEqual(self.emp_2.fullname,'Rohan Nair')
    
    def test_applyRaise(self):
        
        self.emp_1.applyRaise()
        self.emp_2.applyRaise()

        self.assertEqual(self.emp_1.pay,52500)
        self.assertEqual(self.emp_2.pay,63000)
        
    
    
    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
           mocked_get.return_value.ok=True
           mocked_get.return_value.text='Success'
           
           schedule=self.emp_1.monthly_schedule('May')
           mocked_get.assert_called_with('http://company.com/Bhave/May')
           self.assertEqual(schedule,'Success')
           
           
           mocked_get.return_value.ok=False
           
           schedule=self.emp_2.monthly_schedule('June')
           mocked_get.assert_called_with('http://company.com/Nayak/June')
           self.assertEqual(schedule,'Bad Response')
        

if __name__=="__main__":
    unittest.main()
        
        
        
        