d = {"b":4, "a":6, "d":1, "f":3}
print(dict(sorted(d.items(), key = lambda kv:(kv[1],kv[0]))))
l = []
d1 = {}
for k,v in d.items():
    l.append((v,k))
for i in sorted(l):
    d1[i[1]] = i[0]
print(d1)

#swap key value
l1 = d.items()
for k,v in list(l1):
    del d[k]
    d[v] = k
print(d)

