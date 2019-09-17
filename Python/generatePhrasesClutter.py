# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:07:23 2019

@author: abhis
"""
def generatePhrases(phrases):
    phraseDict = {}
    result = []
    for i in range(0, len(phrases)):
        firstString = phrases[i]
        first = firstString.split(' ')
        res = ""
        for s in first[1:]:
            res += str(s)
            res+=" "
        phraseDict[first[0]] = res
    print(phraseDict)
    
    for i in range(0, len(phrases)):
        secondString = phrases[i]
        second = secondString.split(' ')
        if second[-1] in phraseDict.keys():
            #print(secondString , phraseDict[second[-1]])
            res = secondString + phraseDict[second[-1]]
            result.append(res)
    return res
        
        
print(generatePhrases(['writing code','code rocks','a quick bite to eat','a chip off the old block']))


def generate_phrases(phrases):
    # Write your code here
    ans=[]
    first={}
    last={}
    for i in phrases:
        temp = list(i.split(" ")) 
        if temp[0] in first:
            x=list(first[temp[0]])
            x.append(' '.join(temp[1:]))
            first[temp[0]]=x
        else:
            x=[]
            x.append(' '.join(temp[1:]))
            first[temp[0]]=x
    #print(first)
    for i in range(0, len(phrases)):
        f = phrases[i]
        rest = f.split(' ')
        if rest[-1] in first.keys():
            for j in first[rest[-1]]:
                ans.append(f + ' '+j)
    return ans
