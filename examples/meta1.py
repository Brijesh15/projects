class MyMeta(type):
    def __call__(clsname, *args):
        print 'MyMeta called with'
        print 'clsname:', clsname
        print 'args:' ,args
        instance =  object.__new__(clsname)
        print"initialiser calling"
        instance.__init__(*args)
        print"initialiser has called"
        return instance
 
class Kls(object):
    #__metaclass__ = MyMeta
 
    #def __new__(cls):
    #    print"new going on"
        #self.data = data

    def __init__(self,data):
        print"initialiser going on"
        self.data = data
 
    def printd(self):
        print self.data
 
print Kls.__bases__  
ik = Kls('arun')
ik.printd()
