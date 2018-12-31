# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:26:39 2018

@author: abhis
"""
#leetcode 455

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        i=0
        j=0
        count=0
        while(i<len(g) and j<len(s)):
            if(g[i]<=s[j]):
                count+=1
                i+=1
            j+=1
        return count

            
    def findContentChildren2(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()    
        s.sort()    
        child  = 0  
        cookie = 0 
        while  child <len(g) and cookie < len(s):
            print(g[child],s[cookie])
            if g[child] <= s[cookie]:
                print('Here {} and {}'.format(g[child],s[cookie]))
                child += 1
            cookie += 1
        return child
        
        
if __name__=="__main__":
    s=Solution()
    x=s.findContentChildren2([10,9,8,7],[5,6,7,8])
    print(x)
        
        