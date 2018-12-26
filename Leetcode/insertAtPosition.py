# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:29:02 2018

@author: abhis
"""

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    
    def __init__(self):
        self.head=None
        
    def append(self,data):
        newNode=Node(data)
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
                print(current.data)
                current=current.next

    def insertNodeAtPosition(head, data, position):
        current=head
        while(current.next!=None):
            if(current==position):
                tmp=current.data
                current.data=data
                current.next.data=tmp
                current=current.next.next
            else:
                current=current.next
            #return head

s=SinglyLinkedList()
s.append(5)
s.append(6)
s.insertNodeAtPosition(5,1)
s.display()
