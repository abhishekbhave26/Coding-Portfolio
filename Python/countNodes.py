# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:47:29 2019

@author: abhis
"""
#leetcode 222

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.res=0
        def preorder(node):
            if(node):
                if(node.left):
                    preorder(node.left)
                self.res+=1
                if(node.right):
                    preorder(node.right)
        preorder(root)
        return self.res