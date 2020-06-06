class A():
    def __init__(self, name):
        self.n = name

class B(A):
    def __init__(self):
        #A('chaudhary')
        pass

    def fun(self):
        A.__init__(self, 'chaudhary')
        print(self.n)


o1 = A('brijesh')
print(o1.n)
o2=B()
o2.fun()
print(o1.n)
print(o2.n)
