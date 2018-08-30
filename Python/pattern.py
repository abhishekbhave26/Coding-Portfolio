def main():
    for i in range(10):
    	print(str(i) * i)
    return
#main()


def count_letters_digits(s):
	myList=s.split()
	letters_count=0
	digits_count=0
	for i in myList:
		for x in i:
			if x.isdigit():
				letters_count+=1
			elif x.isalpha():
				digits_count+=1
			else:
				pass
	print(letters_count)
	print(digits_count)

count_letters_digits("This is a 75 car")



