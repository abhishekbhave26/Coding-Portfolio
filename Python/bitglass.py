# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:07:14 2020

@author: abhis
"""

def getFactorial(n):
    fact = 1
    if n==0:
        return fact
    else:
        for i in range(1,n+1):
            fact*=i
        return fact


def maxStrength(n):
    # Write your code here
    tempList = [n]
    q = [n]
    while(q):
        x = q.pop()
        if x < 1 or x > 1000000:
            break
        x = str(x)
        count = 0
        for i in x:
            count += getFactorial(int(i))
        tempList.append(count)
        q.append(count)
        print(tempList)
    return n

maxStrength(5)






#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'textFormatting' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY starting
#  2. INTEGER_ARRAY ending
#  3. CHARACTER_ARRAY style
#

def selection(s,count,prev,selected):
    if prev==selected:
        pass
    else:
        count+=1
    return count


def isOverlap(t1,t2,prev,char):
    if t2[0] < t1[1] and prev==char:
        return True
    return False

def applyFormatting(s,char,start,end,selected,prev):
    count = 0
    flag = False
    for i in range(start-1,end):
        if char not in s[i]:
            flag = True
            s[i] += char
    if flag:
        count+=1
        t1 = selected
        t2 = (start,end)
        if isOverlap(t1,t2,prev,char):
            prev = char
            count-=1
            return s,count,selected,prev 
        if selected==(0,0) or selected!=(start,end):
            count+=1
            selected = (start,end)
    else:
        if selected==(0,0) or selected!=(start,end):
            count+=1
            selected = (start,end)
    prev = char
    return s,count,selected,prev

def textFormatting(starting, ending, style):
    # Write your code here
    tempList = [''] *max(ending)
    count = 0
    prev = ''
    selected = (0,0)
    for st,en,sty in zip(starting,ending,style):
        # count += selection(tempList,count,prev,sty)
        tempList,x,selected,prev = applyFormatting(tempList,sty,st,en,selected,prev)
        count +=x
    return count
if __name__ == '__main__':