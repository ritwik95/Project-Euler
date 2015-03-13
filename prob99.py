import linecache
import math
heidi=[]
for x in range(1,1001):
	a=str(linecache.getline('base_exp.txt',x))
	lst=[x.strip() for x in a.split(',')]
	heidi.append(float((int(lst[1]))*math.log(int(lst[0]))))
rit=[]
for y in range(0,1000):
	rit.append(float(heidi[y]))
b=max(rit)
print rit.index(b)+1