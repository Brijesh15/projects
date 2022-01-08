def reduce5(n):
    if n == 0 or n < 0:
        l.append(n)
        return n
    else:
        l.append(n)
        N = 5+ reduce5(n-5)
        l.append(N)
        return N

l = []
reduce5(16)
print(l)
