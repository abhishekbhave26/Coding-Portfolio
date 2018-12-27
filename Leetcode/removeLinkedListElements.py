# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:19:38 2018

@author: abhis
"""
#leetcode 203
#remove linked list elements

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.head=None
        
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        copy=head
        while(self.head.next!=None):
            current=self.head
            if(current.next==val):
                current.next=head.next.next
            else:
                current=current.next
        return copy
        
    
    def append(self,data):
        newNode=ListNode(data)
        if(self.head==None):
            self.head=newNode
        else:
            current=self.head
            while(current.next!=None):
                current=current.next
            current.next=newNode
        
    def display(self):
        if(self.head==None):
            print('Empty')
        current=self.head
        while(current!=None):
            print(current.val)
            current=current.next
            
        

s=Solution()
#s.removeElements(1,4)
s.append(1)
s.append(2)
s.append(3)
#s.display()
s.removeElements(1,2)
s.display()
        