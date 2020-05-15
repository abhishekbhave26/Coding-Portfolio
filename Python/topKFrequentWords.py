# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:18:20 2019

@author: abhis
"""
#leetcode 692

class Solution2:
    def topKFrequent(self, words, k):
        dic = {}
        for i in words:
            if(i in dic):
                dic[i]+=1
            else:
                dic[i]=1
        ret = sorted(dic, key=lambda word: (-dic[word], word))
        return ret[:k]
                     
    
    def topKFrequent2(self, words,k):
        dic={}
        res=[]
        for i in words:
            if(i in dic):
                dic[i]+=1
            else:
                dic[i]=1
        temp=sorted(dic.items(), key = lambda kv:(kv[1], kv[0]))[::-1]
        flag=temp[0][1]
        tempList=[]
        while(k!=0):
            x,y=temp.pop(0)
            if flag==y:
                tempList.append(x)
                flag=y
            else:
                tempList.sort()
                res+=tempList
                res.append(x)
                tempList=[]
                flag=y
            k-=1
        print(tempList)
        if(tempList):
            tempList.sort()
            res+=tempList
        return res
    
    
class Solution(object):
    def topKFrequent(self, nums, k):
        hs = {}
        frq = {}
        for i in range(0, len(nums)):
            if nums[i] not in hs:
                hs[nums[i]] = 1
            else:
                hs[nums[i]] += 1

        for z,v in hs.items():
            if v not in frq:
                frq[v] = [z]
            else:
                frq[v].append(z)
        arr = []
        for x in range(len(nums), 0, -1):
            if x in frq:
                arr.extend(frq[x])                
                
        return [arr[x] for x in range(0, k)]

s=Solution()
x=s.topKFrequent([1,1,1,2,2,3,3],2)
print(x)