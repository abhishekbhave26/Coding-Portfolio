# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:17:59 2018

@author: abhis
"""
#leetcode 118

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if(numRows==0):
            return []
        if(numRows==1):
            return [[1]]
        new=[]*(numRows)
        new.append([1])
        new.append([1,1])
        for i in range(2,numRows):
            c=[]
            c.append(1)
            for j in range(1,i):
                x=new[i-1][j-1]+new[i-1][j]
                c.append(x)
                
                #print('thisvvv')
            c.append(1)
            new.append(c)
            
        return new
    
    
    def generate2(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
    

s=Solution()
if __name__ == "__main__":
    # execute only if run as a script
    x=s.generate(3)   
    print(x)