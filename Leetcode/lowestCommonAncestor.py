# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 18:59:29 2019

@author: abhis
"""

#leetcode 236

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if(root==None):
            return None
        if(root==p or root==q):
            return root
        
        s=Solution()
        left=s.lowestCommonAncestor(root.left,p,q)
        right=s.lowestCommonAncestor(root.right,p,q)
        
        if(left!=None and right!=None):
            return root
        if(left==None and right==None):
            return None
        if(left!=None):
            return left
        else:
            return right
        
         
        