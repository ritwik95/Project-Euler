def fu(sun):
	lst=[]
	sun=0
	while sun<=100:
		lst.append(sun)
		sun+=1
	print sum(lst)**2

print fu(0)