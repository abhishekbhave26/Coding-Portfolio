# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 18:48:34 2018

@author: abhis
"""
#find pair of socks from unsorted array and return the number of pairs

def sockMerchant(n, ar):
    ar.sort()
    print(ar)
    count_pair=0    
    for i in range(1,n):
        if(ar[i]==ar[i-1]):
            count_pair+=1
            i+=1
    if(count_pair%2==0):
        e=(int(count_pair/2))
        return e
    else:
        o=((count_pair+1)/2)
        #print(o)
        return int(o)

x=(sockMerchant(9,[10,20,20,10 ,10 ,30, 50, 10,20 ]))
print(x)