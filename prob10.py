list=[]
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for num in range(2,2000000):
    if is_prime(num):
        list.append(num)
print sum(list)