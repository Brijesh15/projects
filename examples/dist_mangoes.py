import math

def distmango(m, n):
    if m<n:
        return 0
    res = math.factorial(m+n-1)/(math.factorial(m+n-1-(n-1))*math.factorial(n-1))
    return int(res)

print(distmango(7,5))
