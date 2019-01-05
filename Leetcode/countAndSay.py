# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 01:29:30 2019

@author: abhis
"""
#leetcode 38

class Solution:
    def countAndSay(self, n):
    	prev_ans = '1'
    	for i in range(1, n):
    		prev_ans = Solution.read_num(prev_ans)     
    	return prev_ans

    def read_num(num):
        count, string, check = 0, "", num[0]
        for digit in num:
            if check == digit:
                count += 1
            else:
                string += str(count)+check
                check = digit
                count = 1
        string += str(count)+check
        return string
 


       
if __name__=="__main__":
    s=Solution()
    print(s.countAndSay(5))
        