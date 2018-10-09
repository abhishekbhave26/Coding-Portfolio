
a='ababa'

length = len(a)
alist = []
min=2
max=3
max_copy=max+1
for i in a:
	for j in i:
		alist.append(a[min:max_copy+1])
print(alist)


