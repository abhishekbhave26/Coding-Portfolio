class Solution:
    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(nums[0]==0 and len(nums)==1):
            return 1
        else:
            i=nums[0]
        for i,v in enumerate(nums):
        	if(v==i):
        		v+=1
        	else:
        		return i
        return v
    
    '''
    Intuition
    We can harness the fact that XOR is its own inverse to find the missing element in linear time.    
    Algorithm    
    Because we know that nums contains nn numbers and that it is missing exactly one number on the range [0..n-1][0..n−1], we know that nn definitely replaces the missing number in nums. Therefore, if we initialize an integer to nn and XOR it with every index and value, we will be left with the missing number. Consider the following example (the values have been sorted for intuitive convenience, but need not be):    
    Index	0	1	2	3
    Value	0	1	3	4
    \begin{aligned} missing &= 4 \wedge (0 \wedge 0) \wedge (1 \wedge 1) \wedge (2 \wedge 3) \wedge (3 \wedge 4) \\ &= (4 \wedge 4) \wedge (0 \wedge 0) \wedge (1 \wedge 1) \wedge (3 \wedge 3) \wedge 2 \\ &= 0 \wedge 0 \wedge 0 \wedge 0 \wedge 2 \\ &= 2 \end{aligned} 
    missing   
    =4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)
    =(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2
    =0∧0∧0∧0∧2
    =2​
    '''
    
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
    

nums=[0,1,3]
x=Solution()
y=x.missingNumber(nums)
print(y)      	
        	
        	