# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:22:35 2019

@author: abhis
"""
#leetcode 166

class Solution2(object):
    # my soln
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        x=str(float(n)/d)
        stack=[]
        res=''
        for i in x:
            stack.append(i)
        #check if only 1 element in tempList
        c=stack.index('.')
        tempList=stack[c+1:]
        temp=set(tempList)
        if(len(temp)==0):
            return str(float(n)/d)
        if(len(temp)==1 and len(tempList)==1):
            if(tempList[0]=='0'):
                return ''.join(stack[0:c])
            else:
                return ''.join(stack)
        if(len(temp)==1 and len(tempList)>1):
            res =''.join(stack[0:c])
            return res+'.('+str(tempList[0])+')'
    
        
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sign = '-' if numerator * denominator < 0 else ''
        number, rem = divmod(abs(numerator), abs(denominator))
        #print(number,rem)
		# will store the visited remainder information plus the index where it occurred the decimals
        tail = ''
        seen = {}
        while rem > 0:
			# this means we have a repitition, so let's stop
            if rem in seen:
                break		
			# store the index where we first seen this remainder
            seen[rem] = len(tail)	
            n, rem = divmod(rem * 10, abs(denominator))	
			# our decimals
            tail += str(n)
        result = sign + str(number) + '.'
		# rem == 0 means our long division is clean (no repitition)
        if rem <= 0:
            result += tail
        else:
            #print(tail[seen[rem]:])
            result += tail[:seen[rem]] + '(' + tail[seen[rem]:] + ')'	
		# clean trailing dot
        return result.rstrip('.')    
        
s=Solution()
#print(s.fractionToDecimal(1,2))
#print(s.fractionToDecimal(2,1))
print(s.fractionToDecimal(2,3))
#print(s.fractionToDecimal(4,333))


