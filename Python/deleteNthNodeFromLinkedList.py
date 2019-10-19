# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:55:40 2019

@author: abhis
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        le=0
        curr=head
        dummy=ListNode(0)
        dummy.next=head
        while(curr!=None):
            curr=curr.next
            le+=1
        curr=dummy
        c=0
        while(curr.next!=None):
            if(le-c==n):
                curr.next=curr.next.next
            else:
                curr=curr.next
            c+=1
        return dummy.next
        