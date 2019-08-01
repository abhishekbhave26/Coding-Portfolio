#leetcode 495

class Solution
    def findPoisonedDuration(self, timeSeries, duration):
    n=len(timeSeries)
        if(n==0) return 0
        total=0
        for i in range(0,n-1)
            total+=min(timeSeries[i+1]-timeSeries[i],duration)
        return total+duration
       
s=Solution()
print(s.findPoisonedDuration([1,4],2))