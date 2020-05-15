# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 12:52:51 2020

@author: abhis
"""

#!/bin/python3

import math
import os
import random
import re
import sys

https://leetcode.com/problems/sliding-puzzle/discuss/582656/Java-BFS-beat-95
#
# Complete the 'movesToSolve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY puzzle as parameter.
import collections 

def movesToSolve(puzzle):
    res = []
    a,b = len(puzzle),len(puzzle[0])
    seen = {}
    directions = [-1,1,-3,3]
    # treat the puzzle as a list
    for i in puzzle:
        res.extend(i)
    x = "".join(str(i) for i in res)
    q=[]
    q.append(x)
    seen = collections.Counter(q)
    return bfs(q,directions,seen,a,b)

# use bfs find either left or right or top or bottom
# this is modified version of standard bfs or level order traversal
def bfs(q,directons,seen,a,b):
    count=0
    while q:
        size = len(q)
        for i in range(0,size):
            s1 = q.pop(0)
            s1Sort = sorted(s1)
            if s1 == ''.join(s1Sort):
                return count
            index0= s1.index('0')
            for i in directons:
                idx = index0 + i
                # to check if index swapping is valid or not
                if idx<0 or idx>(a*b)-1 or ((index0+1)%a==0 and i==1) or (index0%a==0 and i==-1):
                    continue
                s2 = helper(s1,index0,idx)
                if s2 not in seen:
                    seen[s2]=1
                    q.append(s2)
        count+=1
    return -1


# helper function which creates a new string with the desired swapping
def helper(s1,index0,i):
    g = list(s1)
    s2 = g.copy()
    s2[index0] = g[i]
    s2[i] = g[index0]
    return ''.join(s2)

    '''
    x = sorted(res)
    count= 0
    for i,j in zip(x,res):
        if i!=j and i!=0:
            count+=1
    return count
    '''




#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arraySum' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY inputs
#  2. INTEGER_ARRAY tests
#

def arraySum(inputs, tests):
    setInputs = set()
    # populate setInputs with all elements. 
    # we don't really care about the frequency of each element so use a set
    for i in inputs:
        if i not in setInputs:
            setInputs.add(i)
    # for each input and for each test find if test-input occurs in input
    for i in setInputs:
        for j in tests:
            if j-i in setInputs:
                return True
    return False