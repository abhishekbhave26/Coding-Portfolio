n=52
i=0
for i in range(i,n):
	if (i%3==0 and i%5==0):
		print('FizzBuzz')
	elif i%3==0:
		print ('Fizz')
	elif i%5==0:
		print ('Fizz')
	else:
		print(i)