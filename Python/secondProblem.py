'''
Problem 2: (Algo problem).
 Inputs are N & M, N is the size of a bit vector, M specifies the number of 1s, between 0 and N. 
 Write a program that generates all combinations of bit vectors which have exactly M bits set. 
 E.g. N=4, M=2, answer is 1100,1010,1001,0110,0101,0011. The code is not that big (if done correctly), 
 please email me working code along with examples. For design roles, please implement a design that produces the sequence.
'''

class Solution(object):
    def generateCombinations(self,n,m):
        result = []
        if n==0 or n<m:
            return result
        arr = [None]*n
        s.helper(arr,0,m,result)
        return result
    
    def helper(self,arr,i,m,result):
        # base case for recursion
        if i == len(arr):
            if arr.count(1)==m:
                arr=[str(i) for i in arr] 
                result.append(''.join(arr))
            return
        
        # 2 recursive calls, one each for 0 and 1
        s=Solution()
        arr[i] = 0
        s.helper(arr, i + 1,m,result)  
        
        arr[i] = 1
        s.helper(arr, i + 1,m,result)  
      
    
if __name__== "__main__":
    s=Solution()
    #print(s.generateCombinations(4,2)) # ['0011', '0101', '0110', '1001', '1010', '1100']
    #print(s.generateCombinations(5,3)) # ['00111', '01011', '01101', '01110', '10011', '10101', '10110', '11001', '11010', '11100']
    #print(s.generateCombinations(1,1)) # ['1']
    #print(s.generateCombinations(0,0)) # []
    #print(s.generateCombinations(3,6)) # []
    print(s.generateCombinations(16,15))
            
'''
My thought process:
At the start we have a null or invalid input check. 
Here we consider the bit vector as an array and start filling it up with either 0 or 1. We use recursion to create the bit vectors.
The for each recursive call we will have 2 recursive calls -  one each for adding 0 and 1 to the array.
The base case here if when we reach N which is the size of our bit vector. Here we check if number of 1 bits are equal to M. 
If they are equal we add bit vector to result.
Two small optimization here are we check if number of 0 in array <len(arr)-m and if number of 1 in array is <=m+1 to stop unnecessary recurvive calls.
For eg if we have N=3 and M=1, the recursive cases of 111,011,110,101,000 are not relevant to us. 

Time Complexity O(2^N) worst case complexity. this can be optimized using dynamic programming. 
Space Complexity O(N) for the array
'''
