import itertools
n=123
z=[int(''.join(x)) for x in list(itertools.permutations(list(str(n))))]
print len(z)
print z
