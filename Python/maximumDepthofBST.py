# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:13:21 2019

@author: abhis
"""

#leetcode 104

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        
        if root:
            left=Solution.maxDepth(Solution,root.left)
            right=Solution.maxDepth(Solution,root.right)
            return max(left,right)+1
            
        else:
            return 0
        
    def maxDepthIteration(self, root):
        
        stack = []
        if root is not None:
            stack.append((1, root))
        
        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))
        
        return depth    
        