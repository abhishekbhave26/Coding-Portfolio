# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 23:52:08 2019

@author: abhis
"""
import requests

class Employee():
    
    raise_amt=1.05
    
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def applyRaise(self):
        self.pay=int(self.pay*self.raise_amt)
    
    def monthly_schedule(self,month):
        response=requests.get(f'http://company.com/{self.last}/{month}')
        if(response.ok):
            return response.text
        else:
            return 'Bad Response'