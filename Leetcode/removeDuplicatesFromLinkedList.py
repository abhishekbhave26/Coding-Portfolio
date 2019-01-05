# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 19:20:20 2019

@author: abhis
"""

#leetcode 83

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current=head
        if(current==None):
            return None
        while(current.next!=None and current!=None):
            if(current.val==current.next.val): 
                current.next=current.next.next
            else:
                current=current.next
        
        return head
