
lst=[]
def fun(x):
	y=list(str(x))
	z=[]
	for b in range(0,len(y)):
		z.append((int(y[b]))**2)
	if(sum(z)==1):
		return False
	elif (sum(z)==89):
		return True
	else:
		return fun(sum(z))
for x in range(1,10000000):
	if (fun(x)==True):
		lst.append(x)
print len(lst)	
	

