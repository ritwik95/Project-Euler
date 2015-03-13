a,b=0,1
list=[]
while b<4000000:
	a,b=b,a+b
	list.append(b)
print list
lst=[]
for i in list:
	if i%2==0:
		print i
		lst.append(i)
print sum(lst)