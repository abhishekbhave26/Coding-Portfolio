# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:51:46 2019

@author: abhis
"""
#leetcode 165

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #v1=version1.split('.')
        #v2=version2.split('.')
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        print(versions1)
        for i in range(max(len(versions1),len(versions2))):
            if i < len(versions1):
                v1 = versions1[i]
            else:
                v1 = 0
            if i < len(versions2):
                v2 = versions2[i] 
            else:
                v2 = 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1;
        return 0
    

s=Solution()      
print(s.compareVersion('1.20.5','1.3.6.2'))
            
        