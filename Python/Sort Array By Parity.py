class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n=len(A)
        x=[]
        y=[]
        for i in A:
            if(i%2==0):
                x.append(i)
            else:
                y.append(i)
        for i in y:
            x.append(i)
        print(x)

A=[5,8,6,4,7,9,55,4,1,3,2]
Solution.sortArrayByParity(Solution,A)