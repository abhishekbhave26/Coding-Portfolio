# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 23:39:14 2019

@author: abhis
"""
#leetcode 145

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        s=Solution()
        x=s.helper(root,result)
        return x
    
    def helper(self,root,result):
        s=Solution()
        if(root):
            if(root.left):
                s.helper(root.left,result)
            if(root.right):
                s.helper(root.right,result)
            result.append(root.val)
        return result