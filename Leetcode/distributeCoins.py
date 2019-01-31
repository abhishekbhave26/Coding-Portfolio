# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:28:20 2019

@author: abhis
"""
#leetcode 797

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.c=0
        def dfs(r):
            if r:
                L,R=dfs(r.left),dfs(r.right)
                self.c+=abs(L)+abs(R)
                return r.val+L+R-1
            else:
                return 0
        dfs(root)
        return self.c
    
        
        