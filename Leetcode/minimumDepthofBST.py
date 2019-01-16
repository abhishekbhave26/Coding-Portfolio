# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:48:41 2019

@author: abhis
"""
#leetcode 111

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            children = [root.left, root.right]
            # if we're at leaf node
            if not any(children):
                return 1

            min_depth = float('inf')
            for c in children:
                if c:
                    min_depth = min(self.minDepth(c), min_depth)
            return min_depth + 1 
            
        else:
            return 0