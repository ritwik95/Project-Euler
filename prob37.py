import math
lst=[]
for num in range(2,4000):
    if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
		lst.append(num)
def ltr(w):
	r=list(str(w))
	if (w>9)&(w<100):
		y=int(''.join(r[0:2]))
		o=int(''.join(r[1:2]))
		if ((y in lst)&(o in lst)):
			print w
	elif (w>99)&(w<1000):
		y=int(''.join(r[0:3]))
		o=int(''.join(r[1:3]))
		p=int(''.join(r[2:3]))
		if ((y in lst)&(o in lst)&(p in lst)):
			print w
	elif (w>999)&(w<9999):
		y=int(''.join(r[0:4]))
		o=int(''.join(r[1:4]))
		p=int(''.join(r[2:4]))
		u=int(''.join(r[3:4]))
		if ((y in lst)&(o in lst)&(p in lst)&(u in lst)):
			print w
def trial(b):
	for b in range(0,len(lst)):
		ltr(lst[b])
print trial(1)