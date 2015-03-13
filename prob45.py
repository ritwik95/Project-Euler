heidi=[]
for x in range(1,100000):
	a=x*(x+1)/2
	heidi.append(a)

ritwik=[]
for y in range(1,100000):
	b=y*((3*y)-1)/2
	ritwik.append(b)

purnima=[]
for z in range(1,100000):
	c=z*((2*z)-1)
	purnima.append(c)

print list( set(heidi) & set(ritwik) & set(purnima))


