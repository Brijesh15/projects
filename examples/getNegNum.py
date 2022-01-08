l = [1,-3,5,6,-1,-6,-8,4]
n = 0
l1 = []
for i in range(len(l)):
    if l[n] < 0:
        l.remove(l[n])
        continue
    n+=1
print(l)
