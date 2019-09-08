# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:09:20 2019

@author: abhis
"""

    

        
def equals(x,y):
    if(x==None and y==None):
        return True
    if(x==None or y==None):
        return False
    return x.val==y.val and equals(x.left,y.left) and equals(x.right,y.right)
def traverse(s,t):
    return s!=None and ( equals(s,t) or traverse(s.left,t) or traverse(s.right,t))
def isSubTree(root1,root2):
    x=traverse(root1,root2)
    if(x): return 1
    else: return -1