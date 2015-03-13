


def funmain(abc):
	ans=[]
	for abc in range(10,300000):
		main=list(str(abc))
		i=0
		rit=[]
		while i<len(main):
			rit.append(int((int(main[i]))**5))
			i=i+1
		z=sum(rit)
		if z==abc:
			ans.append(abc)
	print ans

print funmain(0)
	
	



