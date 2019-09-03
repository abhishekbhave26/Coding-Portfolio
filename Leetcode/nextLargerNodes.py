# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 18:29:33 2019

@author: abhis
"""
#leetcode 1019

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res=[]
        stack=[]
        idx=0
        current=head
        while(current!=None):
            res.append(0)
            while stack and stack[-1][1]<current.val:
                temp=stack.pop()
                res[temp[0]]=current.val
            stack.append((idx,current.val))
            current=current.next
            idx+=1
        return res
        