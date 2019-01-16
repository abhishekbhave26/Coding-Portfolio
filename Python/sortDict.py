# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 00:40:15 2019

@author: abhis
"""

import operator


# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

x=sorted(xs.items(), key=lambda x: x[1])
print(x)
#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

sorted(xs.items(), key=operator.itemgetter(1))
#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]