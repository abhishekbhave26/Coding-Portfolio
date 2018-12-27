# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 22:25:09 2018

@author: abhis
"""
#leetcode 2
#add 2 numbers using linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        count=0
        copy=l1
        while(l1!=None or l2!=None):
            a=l1.val+l2.val+count
            if(a>9):
                count=1
                a=a-10
            l1.val=a
            l1=l1.next
            l2=l2.next
        return copy
    
    def addTwoNumbers(self, l1, l2):
        carry = 0
        p = dummyHead = ListNode(0)
        p1, p2 = l1, l2
        
        while p1 != None or p2 != None or carry != 0:
            digit = carry
            if p1 != None:
                digit += p1.val
                p1 = p1.next
            if p2 != None:
                digit += p2.val
                p2 = p2.next
            carry = int(digit / 10)
            p.next = ListNode(digit % 10)
            p = p.next
        
        return dummyHead.next
            
        