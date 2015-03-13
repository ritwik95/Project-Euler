lst=[]
def Pal(n):
    while n<1000000:
		m=n
		a = 0
		while(m!=0):
			a = m % 10 + a * 10
			m = m / 10
			if (n == a):
				lst.append(n)
		n=n+1
	print lst
	
print Pal(1)
	
