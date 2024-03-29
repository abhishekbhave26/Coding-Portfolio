# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:04:50 2019

@author: abhis
"""

#leetcode 102

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        if not root:
            return res
        queue=[root]
        while(queue):
            x, size = [], len(queue)
            for i in range(size):
                node=queue.pop(0)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
                x.append(node.val)
            res.append(x)
        return res
            
            
        
        