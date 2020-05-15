# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:53:57 2020

@author: abhis
"""

def topNCompetitors(competitors,topNCompetitors, reviews):
    # WRITE YOUR CODE HERE
    # WRITE YOUR CODE HERE
    res = []
    compdic = {}
    for i in competitors:
        compdic[i] = 0
    # change here , use s j.count and if count >0 update dic
    # removed lower at 3 places
    for i in reviews:
        for j in i.split():
            if j in compdic:
                compdic[j]+=1
    countDic = {}
    for i in compdic:
        if compdic[i] in countDic:
            x = countDic[compdic[i]]
            x.append(i)
            countDic[compdic[i]] = x
        else:
            countDic[compdic[i]] = [i]
    x = sorted(countDic.items(), reverse=True)
    for i in x:
        
        if len(i[1])==1:
            res.extend(i[1])
            topNCompetitors -= i[0]
        else:
            temp = sorted(i[1])
            i=0
            while(topNCompetitors>0 and i<len(temp)-1):
                res.append(temp[i])
                i+=1
                topNCompetitors-=1
    return res
    

topNCompetitors(['tcs','lt'],2,['lt','lt','tcs','tcs'])
    


def reorderElements(logFileSize, logLines):
    # WRITE YOUR CODE HERE
    dic = {}
    num = {}
    res = []
    diccopy = {}
    for i in logLines:
        x = i.split()
        try:
            c= int(x[1])
            num[x[0]] = x
        except:
            dic[x[0]] = x[1:]
            diccopy[x[0]] = x
    x = sorted(dic, key=dic.get)
    print(num,x, diccopy)
    return res

#reorderElements(3, ['a1 9 6','a3 abt','a2 ab b'])