class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        a=[]
        count=0
        a.append(nums[0])

        for i in range(n-1):
        	if(nums[i]==nums[i+1]):
        		pass
        	else:
        		a.append(nums[i+1])
        		

        
        return a


nums=[1,1,2]
x=Solution.removeDuplicates(Solution,nums)
print(x)
