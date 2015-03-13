def fun(r):
	list=[]
	count=0
	while count<r:
		if count%3==0 or count%5==0:
			list.append(count)
		count=count+1
	print sum(list)
t=input()
while t>0:
	r=input()
	fun(r)
	t=t-1
	
