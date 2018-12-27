# to demonstrate lambda expression

# check if number is even 

def even(num):
	if(num%2==0):
		print('Even')
	else:
		print('odd')



check_even=lambda number:number%2==0

print(check_even(4))


#grabs first character of string

check=lambda s:s[0]

print(check('new'))

#reverses string

check_rev=lambda s:s[::-1]

print(check_rev('new'))

'''
syntax
something=lambda variable:condition