# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 20:56:54 2019

@author: abhis
"""
#leetcode 1171

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeZeroSumSublists(self, head):
        dummy = ListNode(-1)
        dummy.next= head
        ###### save all nodes into dictionary base on their prefix sum
        dic = {0: [dummy]}
        # current sum 
        curSum = 0

        # save all the node into hashmap based on their prefix sum
        while head:
            curSum += head.val
            if curSum not in dic:
                dic[curSum] = []
            dic[curSum].append(head)
            head = head.next

        # update nodes with same prefix sum
        for nodes in dic.values():
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[-1].next
        return dummy.next    
    

#daily interview pro
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
  dummy_head = Node(0, node)
  start = dummy_head
  while start:
    sum = 0
    end = start.next
    while end:
      sum += end.value
      if sum == 0:
        start.next = end.next
        sum = 0
      end = end.next
    start = start.next
  return dummy_head.next

# 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
node = Node(4)
node.next = Node(3)
node.next.next=Node(-2)
node.next.next.next=Node(-1)
node.next.next.next.next=Node(4)
node = removeConsecutiveSumTo0(node)
while node:
  print(node.value)
  node = node.next
  
  
  
node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
  print(node.value)
  node = node.next