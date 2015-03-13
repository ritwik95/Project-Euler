import math

def divisors(k):
	max=[]
	rit=[k]
	q=1
	w=math.ceil(k/2)
	while (q<=w):
		if k%q==0:
			rit.append(q);
		q=q+1
	if len(rit)>=500:
		print rit
	else:
		print "nothing"


	

for n in range(75000,75001):
	j=n*(n+1)/2
	divisors(j)




