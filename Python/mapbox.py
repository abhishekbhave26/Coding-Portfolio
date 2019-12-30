# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 01:06:11 2019

@author: abhis
"""

#passes 5 testcases
def getMaximumScore2(integerArray):
    # Write your code here
    i,score=1,0
    while(integerArray):
        if(i%2==0):
            score-=sum(integerArray) 
            if(integerArray[-1]>integerArray[0]):
                integerArray=integerArray[:-1]
            else:
                integerArray.pop(0) 
        else:
            score+=sum(integerArray)
            if(integerArray[-1]>integerArray[0]):
                integerArray=integerArray[:-1]
            else:
                integerArray.pop(0) 
        print(i,integerArray)
        i+=1
    return score


def helper(integerArray):
    i=0
    score=0
    while(integerArray):
        if(i%2==0):
            score-=sum(integerArray) 
        else:
            score+=sum(integerArray)
        x=integerArray[:-1]
        y=integerArray[1:]
        score1=getMaximumScore(x)
        score2=getMaximumScore(y)
        score=max(score1,score2)
        print(i,integerArray)
        i+=1
    return score
    


def getMaximumScore(integerArray):
    # Write your code here
    return helper(integerArray)
    
print(getMaximumScore([1,2,3,4,2,6]))


