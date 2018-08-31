class Solution:
    def missingNumber(self, nums):
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

    def __init__(self):
        pass

nums=[0,1,3]
x=Solution()
y=x.missingNumber(nums)
print(y)      	
        	
        	