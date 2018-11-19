# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 02:06:07 2018

@author: abhis
"""

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in letters:
            if(i>target):
                return i
        return letters[0]
        '''
        low=0
        high=len(letters)
        while(high>=low):
            mid=int(low+(high-low)/2)
            
            if(letters[mid]<target):
                low=mid+1
            else:
                high=mid-1
        return letters[mid]
        '''
               
s=Solution()
print(s.nextGreatestLetter(['d','t','z'],'y'))