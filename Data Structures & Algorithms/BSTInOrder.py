# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:40:18 2019

@author: abhis
"""
#leetcode 94

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result=[]
        x=Solution.helper(Solution,root,result)
        return x
    
    
    def helper(self,root,result):
        if(root):
            if(root.left):
                Solution.helper(Solution,root.left,result)
            result.append(root.val)
            if(root.right):
                Solution.helper(Solution,root.right,result)
                
        return result
        
        