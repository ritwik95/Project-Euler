man=[]
for x in range(1,28124):
	lst=[]
	for y in range(1,((x/2)+1)):
		if x%y==0:
			lst.append(y)
	if sum(lst)>x:
		man.append(x)

rit=[]		
for z in range(0,len(man)-2):
	for u in range(z+1,len(man)):
		rit.append(man[z]+man[u])
zap=[]
a=28124
for q in range(0,len(rit)):
	if rit[q]<a:
		zap.append(rit[q])
zap=sorted(set(zap))
wet=[]
for d in range(0,a):
	wet.append(d)

pit=list(set(wet)-set(zap))
print sum(pit)



