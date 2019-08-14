#leetcode 989

class Solution(object):
    #working soln
    def addToArrayForm2(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        temp=''
        for i in A:
            temp+=str(i)
        x=int(temp)
        x+=K
        x=str(x)
        res=[]
        for i in x:
            res.append(i)
        return res
    
    def addToArrayForm(self, A, K):
        rev=str(K)
        rev=rev[::-1]
        A=A[::-1]
        carry=0
        flag=0
        for i in range(0,len(A)):
            x=0
            if(i<len(rev)):
                x=int(rev[i])
            temp=A[i]+x+carry
            carry=0
            if(temp>=10):
                carry=1
                A[i]=temp%10
                if(i==len(A)-1):
                    flag=1
            else:
                A[i]=temp
        while(i<len(rev)):
            A.append(rev[i])
            i+=1
        A=A[::-1]
        if(flag==1):
            A.insert(0,carry)
        return A

s=Solution()
print(s.addToArrayForm([0],23))
