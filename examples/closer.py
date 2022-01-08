w=5
def f(x):
    w=2
    def g(y):
        w=4
        def h(z):
            global w
            return w*x+y+z
        return h
    return g
print(f(5)(5)(5))
