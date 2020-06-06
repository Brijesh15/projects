def a(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        func(a,b)
    return inner

@a
def dev(a,b):
    print(a/b)
dev(2,8)    
#def d(a,b):
#    print(a/b)
#div = a(d)
#div(12,6)    
