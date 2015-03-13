a,b=0,1
list=[]
while len(str(b))<1000:
	a,b=b,a+b
	list.append(b)
print len(list)

print len(str(1253764))