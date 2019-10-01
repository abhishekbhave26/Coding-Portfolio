# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:18:09 2019

@author: abhis
"""
#leetcode 938

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.res=[]
        ans=0
        def inorder(root):
            if root.left:
                inorder(root.left)
            self.res.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        for i in self.res:
            if i>=L and i<=R:
                ans+=i
        return ans
        
        