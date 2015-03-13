def Pal(n):
	m=n
	a=0
	while(m!=0):
		a = m % 10 + a * 10
		m = m / 10
	if (n == a):
		return True
	else:
		return False
lst=[]
x=1
while x<1000000:
	z=int("{0:b}".format(x))
	if ((Pal(x)==True) & (Pal(z)==True)):
		lst.append(x)
	x=x+1
print lst
