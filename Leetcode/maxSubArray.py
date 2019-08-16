class Solution(object):
    #O(n2) solution
    #time limit exceeded
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=nums[0]
        if(len(nums)==1):
            return nums[0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                x=nums[i:j]
                res=max(res,sum(x))
        return res


    #O(N) solution
    def maxSubArray2(self, nums):
        max_current=max_global=nums[0]
        for i in range(1,len(nums)):
            max_current=max(nums[i],max_current+nums[i])
            if(max_current>max_global):
                max_global=max_current
        return max_global

s=Solution()
print(s.maxSubArray2([-2,-1]))
        