# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:24:10 2019

@author: abhis
"""
#leetcode 206


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        prev=None
        while(current!=None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev 