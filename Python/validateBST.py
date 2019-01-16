# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:20:06 2019

@author: abhis
"""
#leetcode 98

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        new=[]
        def dfs(root,new):
            if root:
        
                dfs(root.left,new)
                new.append(root.val)
                dfs(root.right,new)
        
        dfs(root,new)
        
        for i in range(1,len(new)):
            if(new[i-1]>=new[i]):
                return False
        return True