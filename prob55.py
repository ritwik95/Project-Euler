lst=[]
def fun(x,count):
	y=int(str(x)[::-1])
	z=x+y
	u=int(str(z)[::-1])
	if count<51:
		if (z==u):
			return True
		else:
			count=count+1
			return fun(z,count)
for x in range(0,10001):
	if (fun(x,0)==True):
		lst.append(x)
print 10001-len(lst)


