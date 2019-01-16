# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:35:35 2019

@author: abhis
"""
#leetcode 230

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        new=[]
        def helper(root):
            if root:
                helper(root.left)
                new.append(root.val)
                helper(root.right)
        helper(root)
        return new[k-1]
    