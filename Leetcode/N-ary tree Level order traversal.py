# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 23:55:11 2019

@author: abhis
"""
#leetcode 429

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        self.getLevel(root, res, 0)
        return res
    
    def getLevel(self, root, res, level):
        if not root:
            return []
        if level == len(res):
            res.append([])
        res[level].append(root.val)
        for child in root.children:
            self.getLevel(child, res, level + 1)
        return res
