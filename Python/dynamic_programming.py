def fib(n,memo):
	if(memo[n]!=None):
		return memo[n]
	if(n==1 or n==2):
		result=1

	else:
		result=fib(n-1,memo)+fib(n-2,memo)
		memo[n]=result
	return result





x=int(input('Enter number for Fibonacci :'))
memo=[None]*(x+1)
print(fib(x,memo))

