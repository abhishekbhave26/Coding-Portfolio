# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:01:48 2019

@author: abhis
"""

def palindrome(s):
    # Write your code here
    dic={}
    count=0
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            x=s[i:j]
            if(x not in dic):
                dic[x]=1
                rev=x[::-1]
                if(rev==x):
                    count+=1
    return count

x=palindrome('aabaa')
#print(x)




def waitingTime(tickets, p):
    # Write your code here
    time=0
    while(tickets[p]!=0):
        for i in range(0,len(tickets)):
            if(tickets[p]==0):
                break
            if(tickets[i]>=1):
                tickets[i]-=1
                time+=1
            else:
                if(p!=i and tickets[i]>0):
                    time+=1
                tickets[i]=-1
                
    return time


def waitingTime2(tickets, p):
    # Write your code here
    time=0
    first=tickets[:p]
    second=tickets[p+1:]
    time+=tickets[p]
    for i in first:
        if i < tickets[p]:
            time += i
        else:
            time += tickets[p]
    for j in second:
        if j < tickets[p]:
            time += j
        else:
            time +=tickets[p]-1
            
    return time


#x=waitingTime2([1,1,1,1],0)
x=waitingTime2([2,6,3,4,5],2)
x=waitingTime([3,4,3,2],2)
print(x)