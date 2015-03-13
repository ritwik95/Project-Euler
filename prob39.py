lst=[]
for i in range(1,1000):
	for z in range(1,i/3):
		for y in range(z,i):
			w=z+y
			if (((z**2)+(y**2))==((i-w)**2)):
				lst.append(i)
from collections import defaultdict

d = defaultdict(int)
for i in lst:
    d[i] += 1
result = max(d.iteritems(), key=lambda x: x[1])
print result