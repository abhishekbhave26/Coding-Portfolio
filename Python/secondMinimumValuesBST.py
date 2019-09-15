# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 00:42:41 2019

@author: abhis
"""
#leetcode 671

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res=[]
        def inorder(root):
            if root.left:
                inorder(root.left)
            self.res.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        s=list(set(self.res))
        s.sort()
        if(len(s)>1):
            return s[1]
        else:
            return -1
            
        