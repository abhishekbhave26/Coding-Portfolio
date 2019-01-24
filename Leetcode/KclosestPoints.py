# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 01:09:00 2019

@author: abhis
"""
#leetcode 973
import math

class Solution(object):
    
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]
    
    
    #time limit exceeded
    def kClosest2(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        d={}
        res=[]
       
        for i in points:
            x,y=i[0],i[1]
            dist=math.sqrt(x*x + y*y)
            if dist in d:
                d[dist]+=[x,y]
                
            else:
                d[dist]=[x,y]
        #print(d)
        while(K!=0):
            
            #print(d.keys())
            x=min(d.keys())
            a=d[x]
            i=len(a)
            if(i>2):               
                while(K!=0 and len(a)>0):
                    K-=1
                    t=a.pop()
                    y=a.pop()
                    d[x]=a
                    new=[t,y]
                    res.append(new)
            else:
                res.append(a)
                del d[x]
                K-=1
        return res
    
    
            
            
            
   
     
if __name__=="__main__":
    s=Solution()
    x=s.kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2)
    print(x)