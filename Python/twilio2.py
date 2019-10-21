# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:20:30 2019

@author: abhis
"""

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'match' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY prefixes
#  2. STRING_ARRAY numbers
#

def match2(prefixes, numbers):
    # Write your code here
    res=[]
    for i in numbers:
        temp=''
        for j in prefixes:
            x=''
            for k in range(0,min(len(i),len(j))):
                if(i[k]==j[k]):
                    x+=i[k]
                else:
                    break
            if(len(x)>len(temp)):
                temp=x
        res.append(temp)
    return res



            


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'segments' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING message as parameter.
#

def segments(message):
    res=[]
    c,count=0,154
    e=c+count
    if(len(message)<160):
        res.append(message)
        return res
    while(e<len(message)):
        if(message[e]!=' '):
            while(e>=c and message[e]!=' ' and message[e+1]!=' '):
                e-=1
        res.append(message[c:e+1])
        c=e+1
        e=c+count
    res.append(message[c:len(message)])
    for i,v in enumerate(res):
        x=res[i]
        x+="("+str(i+1)+"/"+str(len(res))+")"
        res[i]=x
    return res
 

class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.word_finished = False
        self.counter = 1


def add(root, word):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.counter += 1
                node = child
                found_in_child = True
                break
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True


def find_prefix(root, prefix):
    node = root
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.char == char:
                char_not_found = False
                node = child
                break
        if char_not_found:
            return False, 0
    return True, node.counter


def match(prefixes,numbers):
    res=[]
    b=False
    c=0
    root = TrieNode('*')
    for i in prefixes:
        add(root, i)
    for i in numbers:
        b,c=find_prefix(root,i)
        res.append(i[:c])
    return res





i=["+1415123","+1415000","+1412","+1510","+1","+44"]
j=['+14121234567']
x=match(i,j)
print(x)
    
    
    
    
