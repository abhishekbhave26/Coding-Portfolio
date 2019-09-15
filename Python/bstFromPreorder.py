# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 01:41:15 2019

@author: abhis
"""
#leetcode 1008

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        def createTree(node,value):
            if node is None:
                return TreeNode(value)
            else:
                if value>node.val:
                    if node.right is None:
                        node.right=TreeNode(value)
                    else:
                        createTree(node.right,value)
                else:
                    if node.left is None:
                        node.left=TreeNode(value)
                    else:
                        createTree(node.left,value)
            return node            
        tree=None        
        for i in preorder:
            tree=createTree(tree,i)
        return tree
    
    
    '''
    Idea is simple.
    First item in preorder list is the root to be considered.
    For next item in preorder list, there are 2 cases to consider:
    If value is less than last item in stack, it is the left child of last item.
    If value is greater than last item in stack, pop it.
    The last popped item will be the parent and the item will be the right child of the parent.
    '''    
    def bstFromPreorder2(self, preorder):
        root = TreeNode(preorder[0])
        stack = [root]
        for value in preorder[1:]:
            if value < stack[-1].val:
                stack[-1].left = TreeNode(value)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < value:
                    last = stack.pop()
                last.right = TreeNode(value)
                stack.append(last.right)
        return root
        
        