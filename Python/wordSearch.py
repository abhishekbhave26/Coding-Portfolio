# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 01:02:05 2019

@author: abhis
"""
#leetcode 79

class Solution:
    def exist(self,board,word):
        dict={}
        for i in range(0,len(board)):
            for j in range(0,len(board[i])-1):
                #print(board[i][j])
                
                if(board[i][j] in dict):
                    x=dixt[board[i][j]]
                    x.append(board[i][j])
        return 1
                
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word='ABCC'                   
s=Solution()
result=s.exist(board,word)
print(result)
