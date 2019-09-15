# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 22:04:58 2019

@author: abhis
"""
def sameTime(cache,mainMem,item,td):
    if(item in mainMem):
        temp=mainMem[item]
        temp+=(2*td[item])
        if(temp>5):
            del mainMem[item]
            cache[item]=temp
        else:
            mainMem[item]=temp
    else:
        mainMem[item]=2
    return cache,mainMem
    

def updateDic(dic,target):
    for i in dic.keys():
        if(i!=target and dic[i]>0):
            dic[i]-=1
    return dic


def checkCache(cache,mainMem):
    temp=[]
    for i in cache.keys():
        if(cache[i]<=3):
            mainMem[i]=cache[i]
            temp.append(i)
    for i in temp:
        del cache[i]
    return cache,mainMem


def diffTime(cache,mainMem,item):
    if(item in mainMem):
        temp=mainMem[item]
        temp+=2
        if(temp>5):
            del mainMem[item]
            cache[item]=temp
        else:
            mainMem[item]=temp
    else:
        mainMem[item]=2
    return cache,mainMem

def cacheContents(callLogs):
    cache={}
    mainMem={}
    timeDic={}
    td={}
    temp={}
    for i in callLogs:
        if(i[0] in td):
            td[i[0]]+=1
        else:
            td[i[0]]=1
    callLogs.sort()
    for i in callLogs:
        time,item=i
        mainMem=updateDic(mainMem,item)
        cache=updateDic(cache,item)
        if(time not in timeDic):
            timeDic[time]=1
            cache,mainMem=diffTime(cache,mainMem,item)
            cache,mainMem=checkCache(cache,mainMem)
        else:
            if(time not in temp):
                temp[time]=1
                cache,mainMem,sameTime(cache,mainMem,item,td)
                cache,mainMem=checkCache(cache,mainMem)
    if(cache.keys()):
        x=list(cache.keys())
        x.sort()
        return x
    else:
        return [-1]


x=cacheContents([[1, 1], [2, 1], [2, 1], [4, 2], [5, 2], [6, 2]])
print(x)