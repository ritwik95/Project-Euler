def sumdigits(n): 
     numList = list(str(n)) 
     total = sum(int(c) for c in numList) 
     print total
def fac(n):
	if n==0:
		return 1
	else:
		return n* fac(n-1)
print sumdigits(fac(100))