# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 19:16:44 2019

@author: abhis
"""
#leetcode 993 

class Solution:
    # my soln, passes 85/103 test cases
    def isCousins2(self, root, x, y):
        queue=[root]
        while(queue):
            temp,size=[],len(queue)
            for i in range(size):
                node=queue.pop(0)
                if(node.left):
                    queue.append(node.left)
                if(node.right):
                    queue.append(node.right)
                temp.append(node.val)
            if x in temp and y in temp:
                return True
        return False
    
    #using parent annotation, passes all test cases
    def isCousins(self, root, x, y):
        parent = {}
        depth = {}
        def dfs(node, par = None):
            if node:
                depth[node.val] = 1 + depth[par.val] if par else 0
                parent[node.val] = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        return depth[x] == depth[y] and parent[x] != parent[y]


