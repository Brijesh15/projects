import sys
#inputlst = [1,1,2,2,2,2,3,3,4]
inputlst = []
j = 0
for price in sys.argv:
    if j == 0:
        j+=1
        continue
    inputlst.append(int(price))
#print "inputlst:",inputlst
inputset = set(inputlst)
outset = set()
for item in inputset:
    l=[i for i, e in enumerate(inputlst) if e == item]
    ln = len(l)
    if ln == 1:
       outset.add(item)
    elif ln%2 == 0:
       outset.add(item*(ln/2))
    elif (ln != 1) and ln%2 != 0:
        outset.add((item*(ln/2)+item))
#print "outlst:",outset
s=0
for i in outset:
    s= s+i
print s
