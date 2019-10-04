# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 00:10:24 2019

@author: abhis
"""
#leetcode 274

class Solution:
    def hIndex(self, publications: List[int]) -> int:
        n = len(publications)
        citations = [0] * (n + 1)

        for pub in publications:
            if pub < n:
                citations[pub] += 1
            else:
                citations[n] += 1

        total = 0
        i = n
        while i >= 0:
            total += citations[i]
            if total >= i:
                return i
            i -= 1

        return i