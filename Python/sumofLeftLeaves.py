# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:39:39 2019

@author: abhis
"""
#leetcode 404

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root):
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                    self.res += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
        