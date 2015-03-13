import math
x=1
lst=[]
while x<101:
	y=x-1
	for q in range(1,y):
		z=(math.factorial(x))/((math.factorial(q))*(math.factorial(x-q)))
		if z>1000000:
			lst.append(z)
	x=x+1

print len(lst)