# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:33:47 2019

@author: abhis
"""
#leetcode 657

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if moves.count('U')== moves.count('D') and moves.count('L')==moves.count('R'):
            return True
        else:
            return False
