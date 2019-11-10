# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:39:31 2019

@author: abhis
"""
#leetcode 104

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res=0
        if root==None:
            return res
        queue=[root]
        while(queue):
            size=len(queue)
            for i in range(size):
                node=queue.pop(0)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
            res+=1
        return res
