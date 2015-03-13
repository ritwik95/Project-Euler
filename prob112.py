
def fun1(a):
	b=list(str(a))
	c=int("".join(sorted(b)))
	if a==c:
		return True
def fun2(a):
	b=list(str(a))
	c=int("".join(sorted(b)[::-1]))
	if a==c:
		return True
lst=[]
for x in range(1,10000000):
	if (float(len(lst))/x)==0.99:
		print x-100
		break
	elif (fun1(x)==True or fun2(x)==True):
		continue
	else:
		lst.append(x)
		

		
