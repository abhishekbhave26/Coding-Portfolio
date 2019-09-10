# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:21:07 2019

@author: abhis
"""

#leetcode 965

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val=[]
        def dfs(root):
            if(root):
                val.append(root.val)
                dfs(root.left)
                dfs(root.right)
                    
        dfs(root)
        return len(set(val))==1

    
    
    def isUnivalTreeMine(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root):
            x=root.val
        
        def new(root,x):
            if(root.val!=x):
                print(x)
                print(root.val)
                return False
                
            else:
                if(not root.left and not root.right):
                    print(root.val)
                    a=True
                    return 
                else:
            
                    if(root.left):
                        y=new(root.left,x)
                    if(root.right):
                        z=new(root.right,x)
            return 
                    
        a=new(root,x)
        return a
    
    

#new code
        
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res=[]
        def inorderTrav(root):
            if root:
                if(root.left):
                    inorderTrav(root.left)
                self.res.append(root.val)
                if(root.right):
                    inorderTrav(root.right)
        inorderTrav(root)
        nodeSet=set(self.res)
        if(len(nodeSet)==1):
            return True
        else:
            return False
 
        
        