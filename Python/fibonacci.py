def fibo(n):
	if(n==""):
		print('Invalid input')
	x,y=0,1
	while y<n:
		print(x)
		x,y = y,x+y
	print(x)

	
	
print(fibo(50))
