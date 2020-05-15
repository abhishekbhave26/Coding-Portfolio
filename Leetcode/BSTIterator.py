# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:56:44 2020

@author: abhis
"""

#leetcode 173

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.res= []
        if not root:
            return None
        def inorder(root):
            if root.left:
                inorder(root.left)
            self.res.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.res:
            return self.res.pop(0)
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.res:
            return True 
        else: 
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()