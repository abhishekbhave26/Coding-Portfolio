#leetcode 26

class Solution(object):
    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if not nums:
            return 0
        j = 1
        while(j<len(nums)):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
            j+=1
        return i+1
    
    def removeDuplicates(self, nums):
    
        i=1
        if not nums:
            return 0
        pointer = nums[0]
        while(i<len(nums)):
            if nums[i] == pointer:
                nums.pop(i)
                i-=1
            pointer = nums[i]
            i+=1
        return len(nums)
        
                

nums=[1,1,2]
x=Solution.removeDuplicates(Solution)
print(x,nums)
