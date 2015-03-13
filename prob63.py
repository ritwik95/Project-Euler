x=1
rit=[]
while x<50:
	for y in range(0,50):
		z=x**y
		q=str(z)
		if len(q)==y:
			rit.append(x**y)
	x=x+1
print len(rit)