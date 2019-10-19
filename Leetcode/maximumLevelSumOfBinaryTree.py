# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:12:53 2019

@author: abhis
"""

#leetcode 1161

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res=[]
        queue=[root]
        while(queue):
            x,size=0,len(queue)
            for i in range(size):
                node=queue.pop(0)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
                x+=node.val
            res.append(x)
        return res.index(max(res))+1
        
        