# demonstrate zip in python 

x=[1,2,3]
y=[4,5,6]

a=zip(x,y)
print(a)

for pair in zip(x,y):
	print max(pair)