# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:20:48 2020

@author: abhis
"""
# leetcode 19

class ListNode(object):
    def __init__(self,x):
        self.next = None
        self.val = x


class Solution(object):
    
    #two pass
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
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
        
    
    # one pass
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy 
        second = dummy
        i = 0
        # advance first
        while(i<n+1):
            first = first.next
            i+=1
        
        #advance both till end
        while(first != None):
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
        