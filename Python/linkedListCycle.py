# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:04:50 2019

@author: abhis
"""
#leetcode 141

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #Solution O(N) which modifies linked list
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        current=head
        while(current!=None):
            if(current.val!=-1001):
                current.val=-1001
                current=current.next
            else:
                return True
        return False
    
    #Solution O(N) does not modify linked list
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow=head
        fast=head
        while(fast!=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
            if(slow==fast):
                return True
        return False
        
        