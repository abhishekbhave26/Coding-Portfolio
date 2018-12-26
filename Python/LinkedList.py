# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 12:29:21 2018

@author: abhis
"""
import numpy as np
 

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
        
    def prepend(self,data):
        newhead=Node(data)
        newhead.next=self.head
        self.head=newhead
        
    
    def delete(self,data):
        current=self.head
        if(self.head==None):
            print('Empty')
            return
        if(self.head.data==data):
            self.head=self.head.next
            print('Data deleted')
        while(current.next!=None):
            if(current.next.data==data):
                current.next=current.next.next
                print('Data deleted')
                return
            current=current.next

        
    
    def find(self,data):
        current=self.head
        if(self.head==None):
            print('Empty')
        if(self.head.data==data):
            print('{} found'.format(data))
        while(current!=None):
                if(current.data==data):
                    print('{} found'.format(data))
                    return
                else:
                    current=current.next
        print('{} not found'.format(data))
        
    def display(self):
        if(self.head==None):
            print('Empty')
        current=self.head
        while(current!=None):
            print(current.data)
            current=current.next
        
    def reverse(self):
        prev=None
        current=self.head
        while(current!=None):
            next=current.next
            current.next=prev
            prev = current 
            current = next
        self.head = prev
    
    def insertNodeAtPosition(self,data, position):
        i = 0
        newNode = Node(data)
        if position is 0:
            head=self.head
            newNode.next = head
            head = newNode
            return head
        curr = self.head
        while i is not position - 1:
            curr = curr.next
            i+= 1
        prev = curr
        next = curr.next
        prev.next = newNode
        newNode.next = next
        return self.head


s=SinglyLinkedList()
s.append(5)
s.append(6)
s.append(7)
s.append(8)
s.append(10)
s.append(20)
#s.display()
#s.delete(5)
#s.delete(1)
#s.delete(20)
#s.delete(10)
#s.delete(6)
#s.delete(4)
#print('Now reversing')
#s.reverse()
#s.display()

x=s.insertNodeAtPosition(500,4)
#s.insertNodeAtTail(30)
s.display()       
        
        