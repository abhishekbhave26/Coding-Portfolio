# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 23:01:08 2019

@author: abhis
"""

class Node: 	
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def inOrder(root): 
	current = root 
	stack = [] 
	res=[]
	while True:
		if current is not None: 
			stack.append(current) 	
			current = current.left 

		elif(stack): 
			current = stack.pop() 
			res.append(current.data)
			current = current.right 
		else: 
			break
	print(res)

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

inOrder(root) 
