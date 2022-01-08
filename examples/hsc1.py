s = "bj kj w kk sf, ws ;l kj w kk bj wewds w"
d = {}
for i in s.split(" "):
    try:
        d[i]+=1
    except:
        d[i] = 1
print(d)
print(max(d, key=d.get))

