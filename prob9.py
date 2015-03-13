a=0
b=1
while a<=335:
	while b<=670:
		if a**2+b**2==(1000-a-b)**2:
			print a*b*(1000-a-b)
		b=b+1
	b=1
	a=a+1
