def div(x):
	y=(x/2)+1
	q=1
	lst=[]
	while q<=y:
		if x%q==0:
			lst.append(q)
		q=q+1
	return sum(lst)
def main(a):
	rit=[]
	for a in range(1,10000):
		z=div(a)
		e=div(z)
		if ((e==a) & (z!=a)):
			rit.append(z)
			rit.append(a)
	print sum(list(set(rit)))
print main(1)