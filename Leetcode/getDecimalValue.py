# -*- coding: utf-8 -*-
"""
Created on Sat May  2 19:50:52 2020

@author: abhis
"""

#leetcode 1290

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = 0
        i=''
        while(head):
            i+=str(head.val)
            head = head.next
        return int(i,2)