# divisible of 7 multiple of 5 between 1500 and 2700

def myfunc():
	for i in range(1500,2701):
		i+=4
		if(i%7==0):
			print(i)

#myfunc()

nl=[]
for x in range(1500, 2700):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))