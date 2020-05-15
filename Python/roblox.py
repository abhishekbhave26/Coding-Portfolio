# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:44:18 2020

@author: abhis
"""

def maxSubstring(s):
    
    dic = {}
    for i in range(0,len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        for j in range(i+1,len(s)):
            x = s[i]+s[i+1:j+1]
            if x not in dic:
                dic[x] = 1  
    
    listOfSubs = list(dic.keys())
    listOfSubs.sort()
    return listOfSubs[-1]

def socialGraphs(counts):
    dic = {}
    for i,v in enumerate(counts):
        if v in dic:
            x = dic[v]
            x.append(i)
            dic[v] = x
        else:
            dic[v] = [i]
    ordDic = sorted(dic.items())
    for i in dic:
        k, v =i, dic[i]
        j = 0
        if len(v)>=k or k!=0:
            while(j<len(v)):
                printList(v[j:j+k])
                print()
                j = j+k
        
def printList(l):
    for i in range(len(l)):
        print(l[i], end=" ")
    return 


def consecutive(num):
    sumWays = 0
    for i in range(1,num):
        numCopy = 0
        j = i
        while(numCopy <= num):
            if numCopy == num:
                sumWays+=1
                break
            numCopy+=j
            j+=1
    return sumWays

    

    