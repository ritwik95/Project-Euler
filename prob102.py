import linecache
def area(x1,y1,x2,y2,x3,y3):
	return ((x1*(y2-y3) + x2*(y3-y1)+ x3*(y1-y2))/float(2.0));

man=0
for x in range(1,3):
	a=str(linecache.getline('p102_triangles.txt',x))
	lst=[x.strip() for x in a.split(',')]
	a1=area(int(lst[0]),int(lst[1]),int(lst[2]),int(lst[3]),int(lst[4]),int(lst[5]))
	a2=area(0,0,int(lst[2]),int(lst[3]),int(lst[4]),int(lst[5]))	
	a3=area(int(lst[0]),int(lst[1]),0,0,int(lst[4]),int(lst[5]))
	a4=area(int(lst[0]),int(lst[1]),int(lst[2]),int(lst[3]),0,0)
	if (a1==a2+a3+a4):
		print "yes"
	else:
		print "no"
		
		
