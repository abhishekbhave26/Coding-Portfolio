string='abcde'
length = len(string)
alist = []
for i in xrange(length):
	for j in xrange(i,length):
    	alist.append(string[i:j + 1])
    	#l1 = len(alist)
  		#if(l1>= minValue and l2<=maxValue):



