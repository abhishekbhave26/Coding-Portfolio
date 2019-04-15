# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:18:42 2019

@author: abhis
"""

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'checkIPs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY ip_array as parameter.
#


def checkIPs(ip_array):
    # Write your code here
    def ip4(s):
        if(s.count(".")!=3):
            return False
        x=s.split(".")
        for i in x:
            if(not i.isdigit()):
                return False
            c=int(i)
            if(c<0 or c>255):
                return False
        return True


    def ip6(s):
        ls = s.split(':')
        if len(ls) == 8 and all(0 < len(g) <= 4 and all(c in '0123456789abcdefABCDEF' for c in g) for g in ls):
            return True
        return False   

    
    res=[]
    for i in ip_array:
        if(ip4(i)):
            res.append("IPv4")
        elif(ip6(i)):
            res.append("IPv6")
        else:
            res.append("Neither")
    return res




ip_array=["2001:0db8:0000:0000:0000:ff00:0042:8329"]
x=checkIPs(ip_array)
print(x)



