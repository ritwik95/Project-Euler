import itertools
lst=[]
man=[]
import math
for num in range(2,1000):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
		lst.append(num)
for x in range(0,len(lst)):
	z=[int(''.join(x)) for x in list(itertools.permutations(list(str(lst[x]))))]
	for y in range(0,len(z)):
		if int(z[y]) in lst:
			flag=1
		else:
			flag=0
			break
	if flag==1:
		print lst[x]