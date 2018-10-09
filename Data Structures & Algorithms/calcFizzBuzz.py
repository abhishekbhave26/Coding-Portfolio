# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:54:14 2018

@author: abhis
"""


count_f=0
count_b=0
count_fb=0
count_o=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count_fb+=1
    elif(i%3==0):
        count_f+=1
    elif(i%5==0):
        count_b+=1
    else:
        count_o+=1
print('FizzBuzz is {} times'.format(count_fb))
print('Fizz is {} times'.format(count_f))    
print('Buzz is {} times'.format(count_b))
print('Other is {} times'.format(count_o))


