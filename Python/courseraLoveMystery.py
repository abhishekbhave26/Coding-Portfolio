# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 13:39:34 2019

@author: abhis
"""
#coursera love mystery

#
# Complete the 'mystery' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY letter as parameter.
#

def mystery(letter):
    result=[]
    for i in range(len(letter)):
        new=(minimum_reductions(letter[i]))
        result.append(new)
    return result
    

def minimum_reductions(letter):
    length = len(letter)
    count = 0
    for i in range(0,int(length/2)):
        left = ord(letter[i])
        right = ord(letter[(length - 1) - i])
        if left != right:
            if left > right:
                count += left - right
            else:
                count += right - left
    return count



if __name__ == '__main__':
    x=mystery(['abc','abcde'])
    print(x)
    
    
    