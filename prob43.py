import itertools
abc=list(map("".join, itertools.permutations('0123456789')))
lst=[]
a=0
while a<len(abc):
	b=list(abc[a])
	c=int(''.join(b[1:4]))
	d=int(''.join(b[2:5]))
	e=int(''.join(b[3:6]))
	f=int(''.join(b[4:7]))
	g=int(''.join(b[5:8]))
	h=int(''.join(b[6:9]))
	i=int(''.join(b[7:10]))
	if (c%2==0)&(d%3==0)&(e%5==0)&(f%7==0)&(g%11==0)&(h%13==0)&(i%17==0):
		lst.append(abc[a])
	a=a+1
cons=0
for l in range(0,len(lst)):
	p=int(lst[l])
	cons=cons+p
print cons