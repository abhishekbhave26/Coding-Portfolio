# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 00:02:27 2019

@author: abhis
"""
#leetcode 108

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        s=Solution()
        root.left=s.sortedArrayToBST(nums[:mid])
        root.right=s.sortedArrayToBST(nums[mid+1:])
        return root
    
        