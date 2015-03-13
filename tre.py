import itertools
abc=list(map("".join, itertools.permutations('0123456789')))
print len(abc)
import itertools
abc=list(map("".join, itertools.permutations('0123456789')))
lst=[]
a=0
while a<len(abc):
	b=list(abc[a])
	c=int(''.join(b[1:4]))
	if (c%2==0):
		continue
	d=int(''.join(b[2:5]))
	if (d%3==0):
		continue
	e=int(''.join(b[3:6]))
	if (e%5==0):
		continue
	f=int(''.join(b[4:7]))
	if (f%7==0):
		continue
	g=int(''.join(b[5:8]))
	if (g%11==0):
		continue
	h=int(''.join(b[6:9]))
	if (h%13==0):
		continue
	i=int(''.join(b[7:10]))
	if (i%17==0):
		lst.append(abc[a])
	a=a+1
cons=0
for l in range(0,len(lst)):
	p=int(lst[l])
	cons=cons+p
print cons