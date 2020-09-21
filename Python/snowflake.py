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


import math

millnames = ['',' Thousand',' Million',' Billion',' Trillion']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

x=24
i=1626
while i<=2012:
    x*=2
    i+=8
print(millify(x))