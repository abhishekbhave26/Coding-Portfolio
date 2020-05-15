# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 17:10:44 2020

@author: abhis
"""

#leetcode 24


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: 
            return head
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while(curr.next and curr.next.next):
            first = curr.next
            second = curr.next.next
            curr.next = second
            first.next = second.next
            second.next = first
            curr = curr.next.next
            
        return dummy.next
            
        