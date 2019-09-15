# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:57:32 2019

@author: abhis
"""
#leetcode 332

class Solution:
    def findItinerary2(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d={}
        for v in range(0,len(tickets)):
            i=tickets[v]
            for j in range(0,len(i)):
                if(tickets[v][j] in d):
                    x=d[tickets[v][j]]
                    d[tickets[v][j]]=(x,tickets[v][j+1])
                else:
                    d[tickets[v][j]]=tickets[v][j+1]
                break
        #print(d)   
        result=[]
        x="JFK"
        #d={'JFK': ('KUL', 'NRT'), 'NRT': 'JFK'}
        
        if x in d:
            result.append("JFK")
        while(bool(d)):
            y=d[x]
            print(y)
            flag=0
            while(isinstance(y, tuple)):
                y=sorted(y)
                #print(y[0])
                if(y[0] in d):
                    d[x]=y[1]
                    y=y[0]
                else:
                    d[x]=y[0]
                    y=y[1]
                
                print(d)
                flag=1
                break
            result.append(y)
            #print(result)
            if(flag!=1):
                del d[x]
            x=y
        return result
    
    
    
    
    def findItinerary(self, tickets):
        
        d = {}
        for ticket in tickets:
            if ticket[0] not in d:
                d[ticket[0]] = [ticket[1]]
            else:
                d[ticket[0]].append(ticket[1])
        for ticket in d:
            d[ticket].sort()
        res = ['JFK']
        end = []
        while d:
            if res[-1] not in d:
                end.append(res[-1])
                res.pop()
                continue
            fr, to = res[-1], d[res[-1]].pop(0)
            res.append(to)
            if len(d[fr]) == 0:
                d.pop(fr)
        
        if end:
            res += end[::-1]
        
        return res
        
                
            
        
if __name__=="__main__":
    s=Solution()
    x=s.findItinerary([["JFK","AAA"],["AAA","JFK"],["JFK","BBB"],["JFK","CCC"],["CCC","JFK"]])
    print(x)
                    
                