# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:55:09 2019

@author: abhis
"""
#leetcode 589

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None: return res

        def recursion(root, res):
            res.append(root.val)
            for child in root.children:
                recursion(child, res)
            

        recursion(root, res)
        return res
        