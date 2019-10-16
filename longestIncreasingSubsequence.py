#leetcode 300

class Solution(object):
    def lengthOfLIS(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(arr) 
        lis = [1]*n 
        for i in range (1, n): 
            for j in range(0, i): 
                if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                    lis[i] = lis[j]+1
        if(len(lis)!=0):
            return max(lis)
        else:
            return 0
        