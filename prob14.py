def fun(n):
	rit=[n]
	if  n!=1:
		if n%2==0:
			rit.append(n/2)
			n=n/2
			fun(n)
		else:
			rit.append((3*n)+1)
			n=3*n+1
			fun(n)
	print rit

fun(13)
	