# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 00:11:05 2019

@author: abhis
"""
#leetcode 234

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current=head
        x=[]
        while(current!=None):
            x.append(current.val)
            current=current.next
        for i in range(0,len(x)):
            if(i>len(x)/2):
                return True
            if(x[i]!=x[len(x)-i-1]):
                return False
        return True
            
        