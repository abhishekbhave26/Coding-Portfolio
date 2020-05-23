# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:41:48 2020

@author: abhis
"""

def push(value,result=[]):
    result.append(value)
    return result

first=push(0)
push(1,first)
print(push(2))