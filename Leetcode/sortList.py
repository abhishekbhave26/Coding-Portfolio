# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:41:24 2019

@author: abhis
"""
#leetcode 148

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l=[]
        current=head
        current2=head
        while(current):
            l.append(current.val)
            current=current.next
        if(len(l)==0):
            return head
        
        l.sort()
        y=l[0]
        l=l[::-1]
        flag=0
        while(current2):
            x=l.pop()
            current2.val=x
            if(x==y and flag==0):
                flag=1
                head=current2
            current2=current2.next
        return head
            
            
        