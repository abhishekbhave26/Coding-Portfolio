#leetcode 15

<<<<<<< HEAD
from itertools import combinations 
 
class Solution:
    #working code
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        return map(list, res)
    
    
    def threeSum2(self, nums):
        res=[]
        dic=[]
        l = list(combinations(nums,3))
        for i in l:
            s=list(i)
            g=set(s)
            if(sum(s)==0 and g not in dic):
                res.append(s)
                dic.append(g)
        return res
    

class Solution2(object):
    def threeSum3(self,A):
=======
class Solution(object):
    def threeSum3(self, A):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        A.sort() 
        # Now fix the first element  
        # one by one and find the 
        # other two elements  
        for i in range(0, arr_size-2): 
            # To find the other two elements, 
            # start two index variables from 
            # two corners of the array and 
            # move them toward each other 

            # index of the first element 
            # in the remaining elements 
            l = i + 1 

            # index of the last element 
            r = arr_size-1 
            while (l < r): 
                if( A[i] + A[l] + A[r] == sum): 
                    print("Triplet is", A[i],  ', ', A[l], ', ', A[r]); 
                    return True

                elif (A[i] + A[l] + A[r] < sum): 
                    l += 1
                else: # A[i] + A[l] + A[r] > sum 
                    r -= 1
        return False
    
    def threeSum(self,A):
>>>>>>> 1b0a2ededd1a8beec8c852f79448ee0ed8b2efc1
        if(len(set(A))==3):
            print('hello')
        arr_size=len(A)
        res=set()
        for i in range(0, arr_size-1): 
            s = set() 
            curr_sum = 0 - A[i] 
            for j in range(i + 1, arr_size): 
                if (curr_sum - A[j]) in s: 
                    temp=[A[i],A[j],curr_sum-A[j]]
                    temp.sort()
                    res.add(tuple(temp))
                s.add(A[j]) 
        return res
<<<<<<< HEAD

s=Solution()
print(s.threeSum([-2,4,2,0,4,9,-8]))
=======
>>>>>>> 1b0a2ededd1a8beec8c852f79448ee0ed8b2efc1
    
    