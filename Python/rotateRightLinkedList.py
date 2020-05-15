# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:41:49 2020

@author: abhis
"""

#leetcode 61

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        length = 1
        lastElement = head
        while(lastElement.next):
            lastElement = lastElement.next
            length+=1
        
        resNode = head
        lastElement.next = head
        k = k%length
        for i in range(length-k-1): 
            resNode=resNode.next
        answer = resNode.next
        resNode.next = None
        return answer
        