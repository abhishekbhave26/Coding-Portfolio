class Solution:
    def hammingDistance(self, x, y):
        
        return bin(x^y).count('1')

s=Solution()
x=s.hammingDistance(5,3)
print(x)