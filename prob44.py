import math
x=1
lst=[]
for x in range(1,3000):
	y=x*((3*x)-1)/2
	lst.append(y)
	
print lst[len(lst)-1]

def dif(g,h):
	if (abs(g-h) in lst):
		return True

def add(g,h):
	if (g+h) in lst:
		return True
man=[]
def fun(a):
	while a<len(lst):
		b=0
		for  b in range(0,len(lst)):
			if ((dif(lst[a],lst[b])==True) & ((add(lst[a],lst[b]))==True)):
				man.append(abs(lst[a]-lst[b]))
		a=a+1
	print  man
	
print fun(0)


