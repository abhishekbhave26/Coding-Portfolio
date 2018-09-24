# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 23:57:39 2018

@author: abhis
"""

def func():
    return 1

#print(func())

def hello():
    return 'hello'

#print(hello())

greet=hello

#print(greet())


def myhello(name='abhishek'):
    print('The hello() fnction is called')
    
    def greet():
        return '\t This is the greet() function'
    
    def welcom():
        return '\t This is welcome() function'
    
    
    print('I am going to return a function')
    if(name=='abhishek'):
        return greet
    else:
        return welcom

#my_new_func=myhello()
#print(my_new_func())



def new_decorator(original_func):
    def wrap_func():
        
        print('Some extra code,before the original func')
        
        original_func()
        
        print('Some extra code,after the original func')
        
    return wrap_func


    


@new_decorator
def func_needs_decorator():
    print('I want to be decorated')

func_needs_decorator()





