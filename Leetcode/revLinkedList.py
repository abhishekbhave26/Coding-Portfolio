# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:54:16 2018

@author: abhis
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        current=head
        next=None
        while(current!=None):
            next=current.next
            current.next=prev
            prev = current 
            current = next
        head = prev
        return head
