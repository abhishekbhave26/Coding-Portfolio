class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
        'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        


        char1=s[1:]
        char2=s[0:]
        mainList=[]

        count=myList.count()
        for letter in myList:
        	x=mydict.keys(letter)
        	mainList.append(x)


def myfunc(s):
    newList=[]
    dict='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for x in dict:
    	newList.append(x)

    if(len(s)>1):
    	for i,value in enumerate(newList,1):
    		if(value==s[0]):
    			temp_result=26*i
    	for i,value in enumerate(newList,1):
    		if(value==s[0]):
    			result=i
    	result+=temp_result
    	print(result)  

    else:
    	for i,value in enumerate(newList,1):
    		if(value==s):
    			print(i)


    		
myfunc("HH")
#print(Solution.titleToNumber("CA"))

