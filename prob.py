a=1
list=[]
while a<10000:
	b=[int(i) for i in str(a)]
	d=len(b)
	c=0
	while c<d:
		list.append((b[c])**2)
		c=c+1
	if sum(list)==a:
		print a
	a=a+1