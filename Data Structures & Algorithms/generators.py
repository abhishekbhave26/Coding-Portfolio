# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 13:21:18 2018

@author: abhis
"""
#yield saves memory


def fibonacci(n):
    a=1
    b=1
    for i in range(n):
        yield a         #yield saves memory we dont have to return everything in a list thus saving memory
        a,b=b,a+b

for number in fibonacci(10):
    print(number)
    
    
def simple_gen():
    for x in range(3):
        yield x
        
#for number in simple_gen():
    print(number)
    
g=simple_gen()


#print(next(g))
#print(next(g))

s='hello'

#for letter in s:
#print(letter)
    
s_iter=iter(s)
#print(next(s_iter))