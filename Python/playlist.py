# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:38:34 2019

@author: abhis
"""

def playlist(songs, k, q):
    res,c,d=0,0,0
    i=k
    res=[]
    while(i!=k-1):
        if(songs[i]==q):
            res.append(c)
            break
        c+=1
        i+=1
        if(i==len(songs)):
            i=0
    i=k
    while(i!=k+1):
        if(songs[i]==q):
            res.append(d)
            break
        d+=1
        if(i==0):
            i=len(songs)
        i-=1
    return min(res)

x=playlist(['wheniseeyouagain','borntorun','nothingelsematters','nothingelsematters'],0,'nothingelsematters')
print(x)



'''
if(k==sIdx):
        return 0
    res=min(k-sIdx,sIdx-k)
    if(res<0):
        res*=-1
    return res
'''