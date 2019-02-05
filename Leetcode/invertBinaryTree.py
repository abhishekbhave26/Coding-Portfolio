# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:54:51 2019

@author: abhis
"""
#leetcode 226


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        
        right=Solution.invertTree(Solution,root.right)
        left=Solution.invertTree(Solution,root.left)
        root.left=right
        root.right=left
        
        return root
    
    def inverTree2(self,root):
        if root==None:
                return None
        root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
        return root