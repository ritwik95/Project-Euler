import math
lst=[]
y=3
while y<3000000:
	rit=list(str(y))
	man=[]
	for x in range(0,len(rit)):
		man.append(math.factorial(int(rit[x])))
		if sum(man)==y:
			lst.append(y)
	y=y+1
	
print sum(lst)