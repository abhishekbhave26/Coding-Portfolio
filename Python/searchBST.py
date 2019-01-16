# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:38:54 2019

@author: abhis
"""
#leetcode 700

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return []
        
        if root.val == val:
            return root
        
        elif root.val > val:
            return self.searchBST(root.left, val)
        
        return self.searchBST(root.right, val)
        