# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 18:32:04 2019

@author: abhis
"""

def flip(s):
    res=''
    for i in s:
        if(i=='0'):res+='1'
        else:res+='0'
    return res


def theFinalProblem(target):
    x='0'*len(target)
    flips=0
    if(x==target):
        return 0
    for i in range(0,len(target)):
        temp=x[0:i]
        temp2=x[i:]
        if(target[i]!=x[i]):
            flips+=1
            j=flip(temp2)
            x=temp+j
        if(x==target):
            return flips
        
#print(theFinalProblem('0011'))
            

def solution(A):
    # write your code in Python 3.6
    s=str(A)
    if(len(s)==0):
        return 0
    if(len(s)==1):
        return 9
    if(s[0]=='6'):
        temp=s[1:]
        temp='9'+temp
        return int(temp)
    m=-1
    for i in range(0,len(s)):
        if s[i]=='6':
            curr=int(s[0:i]+'9'+s[i+1:])
            m=max(m,curr)    
    if(m==-1):
        return A
    else:
        return m

print(solution(99))
print(solution(69))
print(solution(66))
print(solution(96))





def solution(S):
    no=(int(S,2))
    steps=0
    while(no!=0):
        steps+=1
        if(no%2==0):
            no/=2
        else:
            no-=1
    return steps
