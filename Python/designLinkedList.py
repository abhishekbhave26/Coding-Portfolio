# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 17:04:37 2018

@author: abhis
"""
#leetcode 707

class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None
        

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        '''
        current=self.head
        if(self.head==None):
            return -1
        if(self.head==index):
            return self.head.val
        while(self.head!=None):
            print(self.head)
            if(self.head==index):
                print('Here')
                return self.head.val
            self.head=self.head.next
        return -1
        '''
        if index < 0:
            return -1

        current = self.head
        for _ in range(index):
            current = current.next
        return current.val
        

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        current=self.head
        newNode=Node(val)
        if(current==None):
            current=newNode
            self.head=current
        else:
            while(current.next!=None):
                current=current.next
            current.next=newNode
            
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        
        
        
    def display(self):
        current=self.head
        if(current==None):
            print('Empty')
        else:
            while(current!=None):
                print(current.val)
                current=current.next
        
        
        

if __name__=="__main__":
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    obj.addAtTail(5)
    obj.addAtTail(7)
    obj.addAtTail(3)
    obj.addAtTail(10)
    obj.display()
    
    param_1 = obj.get(5)
    print(param_1)
    #obj.addAtHead(2)
    #obj.addAtTail(15)
    #obj.addAtIndex(3,4)
    #obj.deleteAtIndex(4)