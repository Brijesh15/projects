def getsuperDegit(n, k):
    sum = 0
    while n:
        sum+=n%10
        n= n//10
    p = sum*k
    def superDegit(p):
        s = 0
        while p:
            s+=p%10
            p= p//10
        if len(str(s)) == 1:
            return s
        superDegit(s)
    return superDegit(p)

def decoDegit(fun):

    def inner(n, k):
        sum = 0
        while n:
            sum+=n%10
            n= n//10
        p = sum*k
        return fun(p)
    return inner

@decoDegit
def superDegit(p):
    s = 0
    while p:
        s+=p%10
        p= p//10
    if len(str(s)) == 1:
        return s
    return superDegit(s)
    #return superDegit(p)

print(superDegit(123452513, 4))
print(getsuperDegit(123452513, 4))
