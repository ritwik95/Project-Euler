a=1000
list=[]
while a<2000:
	b=[int(i) for i in str(a)]
	d=len(b)
	c=0
	while c<d:
		z=(b[c])**4
		list.append(z)
		c=c+1
	if sum(list)==a:
		print a
	a=a+1