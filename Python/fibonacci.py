# Fibonacci by normal method    O(2^n)

def fib(n):
	if n==1 or n==2:
		result=1
	else:
		result=fib(n-1)+fib(n-2)
	return result

# using dynamic programming or memoization(different to memorization)		O(n)
def fiboncci(n,memo):
	if memo[n]!=None:
		return memo[n]
	if n==1 or n==2:
		result=1
	else:
		result=fib(n-1)+fib(n-2)
		memo[n]=result
	return result

# bottom up approach			O(n)
def fib_bottom(n):
	if n==1 or n==2:
		result=1
	bottom_up=[None]*(n+1)
	bottom_up[1]=1
	bottom_up[2]=1
	for i in range(3,n+1):
		bottom_up[i]=bottom_up[i-1]+bottom_up[i-2]
	return bottom_up[n]



# function to call above 2 functions
def print_fibo(n):
	#print(fib(10))
	memo= [None] *(n+1)
	#print(fiboncci(n,memo))
	print(fib_bottom(n))

print_fibo(1700)




def fibo(n):
	if(n==""):
		print('Invalid input')
	x,y=0,1
	while y<n:
		print(x)
		x,y = y,x+y
	print(x)



