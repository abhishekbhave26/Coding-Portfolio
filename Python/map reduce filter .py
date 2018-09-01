# demostrate map 

	


a=[1,2,3,4]
b=[4,5,6,7]

(map(lambda x,y: x+y,a,b)


# demostrate reduce 


reduce(lambda x,y:x+y,a)



# demostrate filter

def myfunc(num):
	if num%2==0:
		return True
	else:
		return False

print(myfunc(5))

lst=range(10)

filter(myfunc,lst)
