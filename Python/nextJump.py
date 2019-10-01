# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:50:25 2019

@author: abhis
"""

def get_rock_index(quantity):
    qcopy=sorted(quantity)
    geoff=[]
    for i in range(0,len(qcopy)):
        geoff.append(qcopy[i]+quantity[i])
    dic={}
    res={}
    for i,v in enumerate(geoff):
        if v in dic:
            dic[v]+=1
            x=res[v]
            x.append(i)
            res[v]=x
        else:
            dic[v]=1
            res[v]=[i]
    k,v=0,0
    for i in dic.keys():
        temp=dic[i]
        if(temp==v):
            k=max(k,i)
            v=temp
        if(temp>v):
            k=i
            v=dic[i]
    x=res[k]
    return max(x)

#print(get_rock_index([10,10,7,7,7,2,7,2]))

#print(get_rock_index([5,5,9,19,2,2]))

mydict = {'george':16,'amber':19}
x=(list(mydict.keys())[list(mydict.values()).index(16)]) # Prints george
#print(type(x))







import string

# Complete the encode_string function below.
def encode_string(s):
    dic={'a':1,'e':1,'i':1,'o':1,'u':1}
    s=s.lower()
    mapper=dict(zip(string.ascii_lowercase, range(1,27)))
    res=''
    for i in range(0,len(s)):
        if s[i] not in dic:
            dic[s[i]]=1
            if(i==len(s)-1):
                temp=mapper[s[i]]+mapper[s[0]]  
                print(temp)
            else:
                temp=mapper[s[i]]+mapper[s[i+1]]
                print(temp)
            temp=temp%26
            if(temp==0):
                res+='z'
            else:
                res+=list(mapper.keys())[list(mapper.values()).index(temp)]
    return res

print(encode_string('d'))

#print(encode_string('yxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxyxioioioioio'))


