# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:54:28 2019

@author: abhis
"""
#leetcode 897

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.res=[]
        def inorderTrav(root):
            if root:
                if(root.left):
                    inorderTrav(root.left)
                self.res.append(root.val)
                if(root.right):
                    inorderTrav(root.right)
        inorderTrav(root)
        head=TreeNode(None)
        current=head
        for i in self.res:
            current.right=TreeNode(i)
            current=current.right
        return head.right
            