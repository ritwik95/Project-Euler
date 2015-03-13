de=[]
for x in range(1,150000):
	lst=list(str(x))
	man=list(str(2*x))
	rit=list(str(3*x))
	hei=list(str(4*x))
	san=list(str(5*x))
	pur=list(str(6*x))	
	z=list(set(lst)-set(man))
	y=list(set(lst)-set(rit))
	f=list(set(lst)-set(hei))
	g=list(set(lst)-set(san))
	a=list(set(lst)-set(pur))
	if ((len(z))==0) & ((len(y))==0) & ((len(f))==0) & ((len(g))==0) & ((len(a))==0) :
		de.append(x)

print de