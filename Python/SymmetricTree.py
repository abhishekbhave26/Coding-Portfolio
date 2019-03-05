# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 00:25:54 2019

@author: abhis
"""
#leetcode 101

class Solution:
    def isSymmetric(self, root):
        return Solution.helper(Solution,root,root)
    
    def helper(self,r1,r2):
        if(r1==None and r2==None):
            return True
        if(r1==None or r2==None):
            return False
        s=Solution()
        return (r1.val==r2.val) and s.helper(r1.right,r2.left) and s.helper(r1.left,r2.right)
        
    