def sublist(l):
    b = [[]]
    for i in range(len(l)+1):
        #for j in range(i+1, len(l)+1):
        for j in range(i):
            #b.append(l[i:j])
            b.append(l[j:i])
    return b

print(sublist([1,2,3]))
print(list([1,2,3][j:i] for i in range(3+1) for j in range(i)))

def sublist1(l,n):
    b = []
    for i in range(len(l)+1):
        #for j in range(i+1, len(l)+1):
        for j in range(i):
            #b.append(l[i:j])
            if sum(l[j:i]) == n:
                b.append(l[j:i])
    return b

print(sublist1([1,2,3,4,5],5))
#print(list([1,2,3][j:i] for i in range(3+1) for j in range(i)))
