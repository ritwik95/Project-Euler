x=1
lst=[]
while x<100:
	for y in range(1,100):
		z=list(str(x**y))
		a=0
		su=0
		while a<len(z):
			su=su+int(z[a])
			a=a+1
		lst.append(su)
	x=x+1
	
print max(lst)