# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 12:39:09 2019

@author: abhis
"""

#leetcode 922

class Solution:
    def sortArrayByParityII2(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        a=[i for i in A if i%2==0]
        b=[i for i in A if i%2!=0]
        result=[]
        i,j=0,0
        for x in range(0,len(A)):
            if((x)%2==0):
                result.append(a[i])
                i+=1
            else:
                result.append(b[j])
                j+=1
        
        return result
    
    def sortArrayByParityII(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
            
    
if __name__=="__main___":
    s=Solution()
    x=s.sortArrayByParityII([4,2,5,6,9,5])
    print(x)
    print('hello')