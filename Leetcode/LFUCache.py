# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 01:05:42 2019

@author: abhis
"""

#leetcode 460 

#only 15/23 cases passed 
class LFUCache:

    def __init__(self, capacity):
        self.dic={}
        self.n=capacity
        self.lrucache=[]

    def get(self, key):
        
        if(key in self.dic):
            index=self.lrucache.index(key)
            temp=self.lrucache.pop(index)
            self.lrucache.append(temp)
            return self.dic[key]
        else:
            return -1 

    def put(self, key, value):
        if(self.n==0):
            return 
        if(len(self.dic)>=self.n):
            #remove lru ,then add
            temp=self.lrucache.pop(0)
            if(temp in self.dic):
                del self.dic[temp]
        #if(key in self.dic):
            #index=self.lrucache.index(key)
            #temp=self.lrucache.pop(index)
            #key=temp
            #self.dic[key]=value
        
        self.dic[key]=value
        temp=[key]+self.lrucache
        self.lrucache=temp
        print(self.dic)


["LFUCache","put","put","get","get","get","put","put","get","get","get","get"]
[[3],[2,2],[1,1],[2],[1],[2],[3,3],[4,4],[3],[2],[1],[4]]

# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(3)
obj.put(2,2)
obj.put(1,1)
print(obj.get(2))
print(obj.get(1))
print(obj.get(2))
obj.put(3,3)
obj.put(4,4)
print(obj.get(3))
print(obj.get(2))
print(obj.get(1))
print(obj.get(4))
