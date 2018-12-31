# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:22:34 2018

@author: abhis
"""
#leetcode 383

import unittest

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d={}
        for i in magazine:
            if(i in d):
                x=d.get(i)
                x+=1
                d[i]=x
            else:
                d[i]=1
        new=''
        c=len(ransomNote)
        count=0
        for i in ransomNote:
            if i in d:
                new=new+i
                count+=1
                x=d.get(i)
                if(x==1):
                    d.pop(i)
                else:
                    x=x-1
                    d[i]=x
        if(c==count):
            return True
        else:
            return False



class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(Solution.canConstruct(Solution,'aa','aab'), True)
    
                

        
if __name__=="__main__":
    s=Solution()
    x=s.canConstruct('aa','aab')
    print(x)
    
    s=MyTest()   
    s.test()