# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:57:03 2019

@author: abhis
"""
#leetcode 54

class Solution(object):
    def spiralOrder2(self, matrix):
        res=[]
        for i in range(0,len(matrix)):
            if(i%2==1):
                res+=matrix[i][::-1]
            else:
                res+=matrix[i]
        return res
    
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans
        
            
            
        