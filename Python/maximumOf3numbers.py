
"""
Created on Wed Jan 16 12:01:22 2019

@author: abhis
"""
#leetcode 628

class Solution: 
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        x=nums[n-1]*nums[n-2]*nums[n-3]
        y=nums[0]*nums[1]*nums[n-1]
        return max(x,y)

        
    
    def maximumProductWrong(self,nums):
        
        
        
        i=0
        d={}
        for y in nums:
            if y<0:
                y=-y
            if y in d:
                d[y]+=1
            else:
                d[y]=1
        num=1
        while(i<3):
            #print(nums)
            print('This is d: {}'.format(d))
            a=max(d)
            count=d[a]
            #print('This is :{}'.format(count))
            while(count>0):
                num*=max(nums)
                print(num)
                count-=1
                u=d[a]
                if(u>1):
                    d[a]-=1
                else:
                    print(d)
                    del d[a]
                    print(d)
                i+=1
            
            #print(nums)
        return num
    
    


s=Solution()
x=s.maximumProduct([-4,-3,-2,-1,60])
print(x)            
            
            
            
        
        