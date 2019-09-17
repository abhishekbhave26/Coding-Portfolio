# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:48:18 2019

@author: abhis
"""
#leetcode 8

#passes 1070 out of 1079 testcases
class Solution2(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        stack=[]
        if len(str)==0:
            return 0
        x=1
        for i in str:
            if(i=='.'):
                break
            if(stack and i==' '):
                break
            if(i==' '):
                pass
            if(i=='-' and x==0):
                return 0
            if i=='-':
                x=-1
            if(i=='+' and x==-1):
                return 0
            if i=='+':
                x=0
            if i.isalpha():
                if(stack):
                    break
                else:
                    return 0
            if i.isdigit():
                stack.append(i)
        if stack:
            number=''.join(stack)
        else:
            return 0
        if(x==-1):
            number=int(number)*-1   
        else:
            number=int(number)
        if(number > pow(2,31)-1):
            return pow(2,31)-1
        elif(number < pow(-2,31)):
            return pow(-2,31)
        else:
            return number
          
#Find if the string starts with +/- followed by any number of digits or strats with any number of digits
import re
class Solution(object):
    def myAtoi(self, str):
        out = str.strip()
        out = re.findall("^[+-]\d+|^\d+", out)
        print(out)
        try:
            out = int(out[0])
        except:
            out = 0
        return min(max(-2**31, out), 2**31-1)


s=Solution()
print(s.myAtoi("  -0012a42"))   
print(s.myAtoi("   +0 123"))         
print(s.myAtoi('4193 with words'))      
print(s.myAtoi('words and 987'))      
print(s.myAtoi('-91283472332')) 
print(s.myAtoi('-'))   
print(s.myAtoi('+'))
print(s.myAtoi('3.456'))
print(s.myAtoi('+-2'))
print(s.myAtoi('-+1'))              

