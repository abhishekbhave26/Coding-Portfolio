'''
Problem 1:Consider the following : 

You have 3 (can be M) 6-sided blocks with letters on each face of the block (Alphabet blocks). 
Block A = {D,N,K,P,F,T}
Block B = {R,S,K,L,A,I}
Block C = {B,H,O,E,E,R}
Given a <=3(can be N) lettered string, the algo should predict if its possible to spell the string using these blocks.
NOTE: A block cannot be used more than once.  
Eg. "RED" - BlkB [R] BlkC [E] BlkA [D]
    "ELK" - BlkC [E] BlkB [L] BlkA [K]
    "SIR" - COMBINATION NOT POSSIBLE 
    "FEE" - COMBINATION NOT POSSIBLE    
    "ON"  - BlkC [O] BlkA [N]
'''
import collections

class Solution(object):
    
    def __init__(self,listOfBlocks):    
        self.dic = {}
        for i,v in enumerate(listOfBlocks):
            if len(v)!=6:
                continue
            self.dic[i]=dict(collections.Counter(v))
     
    def canSpellString(self,str):
        seen = {}
        if len(str)>len(self.dic):
            return False
        for i in str:
            flag = False
            for j in self.dic:
                if i in self.dic[j] and j not in seen:
                    seen[j]=1
                    flag = True
                    break
            if not flag:
                return flag
        return True
     
     
    
if __name__== "__main__":
    s=Solution([['D','N','K','P','F','T'],['R','S','K','L','A','I'],['B','H','O','E','E','R']])
    print('RED - ' , s.canSpellString('RED'))
    print('ELK - ' ,s.canSpellString('ELK'))
    print('SIR - ' ,s.canSpellString('SIR'))
    print('FEE - ' ,s.canSpellString('FEE'))
    print('ON - ' ,s.canSpellString('ON'))
    print('EE - ' ,s.canSpellString('EE'))
    print(' - ' ,s.canSpellString(''))
    print('DREE - ' ,s.canSpellString('DREE'))
    
    
  
'''
My thought process:
My algorithm is first initialized by a constructor which creates a dictionary(hashmap) with key as integer and value as each block.
I have used the collections package in the constructor. It can also be done manually by creating a dictionary and doing a key,frequency mapping
For each string, it first checks if length of string is greater than number of blocks. If true algorithm returns false as string cannot be spelled.
Next, for each character in string, I check if it exists in each block. If not found in any blocks return False.
Algorithm is optimized for M number of 6 sided blocks. It is also optimized for input string with N length.
If possible to spell string algorithm returns True else if not possible to spell string returns False.

Time Complexity O(N*M) where N is the length of string and M is the number of blocks. This is the worst case complexity.
If I were to have just 3 blocks, the complexity would be O(N) where N is the length of string

Space Complexity O(N) where N is the number of blocks
'''
    