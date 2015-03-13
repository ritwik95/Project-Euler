lst=[]
import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
for num in range(1000,10000):
    if is_prime(num):
        lst.append(num)
hei=[]
def fun(x):
	w=x+3330
	e=w+3330
	if ((w in lst) & (e in lst)):
		p=list(str(x+3300))
		o=list(str(w+3330))
		j=list(str(x))
		t=list(set(j)-set(o))
		k=list(set(j)-set(p))
		if ((len(t)==0) & (len(k)==0)):
			hei.append(x)
			hei.append(w)
			hei.append(e)
for q in range(0,len(lst)):
	fun(lst[q])
print (hei)