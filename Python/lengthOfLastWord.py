# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 15:06:29 2019

@author: abhis
"""
#leetcode 58

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=s.split()
        length=len(x)
        new=(x[length-1:length])
        if(len(new)==0):
            return 0
        for i in new:
            s=str(i)
        return len(s)
        
        
        
if __name__ == '__main__':
    s=Solution()
    x=s.lengthOfLastWord('    ')
    print(x)