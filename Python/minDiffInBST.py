# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:07:56 2020

@author: abhis
"""
#leetcode 783

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        globalMin = 999999
        self.res=[]
        def inOrder(root):
            if root.left:
                inOrder(root.left)
            self.res.append(root.val)
            if root.right:
                inOrder(root.right)
        inOrder(root)
        for i in range(0,len(self.res)-1):
            diff = abs(self.res[i] - self.res[i+1])
            globalMin = min(globalMin, diff)
        return globalMin
            