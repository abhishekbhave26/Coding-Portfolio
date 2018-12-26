class Solution:
    def reverseWords(s):
        """
        :type s: str
        :rtype: str
        """
        myList=[]
        mainList=[]
        count=0
        mainList=s.split()
        if(s==""):
        	return s
        else:
        	for words in mainList:
        		myList.append(words[::-1])
        		myList.append(" ")
        	myList.pop()
        
        return ''.join(myList)

print(Solution.reverseWords(""))