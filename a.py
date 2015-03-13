def square_sum_difference(n):
    return int(n*(n+1)*(2*n+1)/6 - (n*(n+1)/2)**2)
print square_sum_difference(100)