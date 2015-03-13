a=100
list=[]
while a<1000:
	b=100
	while b<1000:
		s=str(a*b)
		if s==s[::-1]:
			list.append(a*b)
		b+=1
	a+=1
print max(list)
	