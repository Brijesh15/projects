class A(object):
    
    def __new__(cls,arg):
        print "A.__new__ is called"
        return super(A,cls).__new__(cls)

    def __init__(self,Name):
        self.name = Name
        print "A.__init__ called"

    def __str__(self):
        return "SAMPLE"

    def __repr__(self):
        return "Sample"

a = A('Brijesh')
b = A('chaudhary')
#print a.__str__()
#print a.__repr__()
print a.name, b.name
