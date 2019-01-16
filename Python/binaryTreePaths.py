# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:32:00 2019

@author: abhis
"""
#leetcode 527

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        def helper(root,result):
            if root:
                result+=str(root.val)
                
                if(not root.left and not root.right):
                    new.append(result)

                else:
                    result+='->'
                
                helper(root.left,result)
                helper(root.right,result)
        new=[]
        helper(root,'')
        return new