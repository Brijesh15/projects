class Singleton(type):
    _instance = {}
    def __call__(cls, *args, **kwargs):
        print"singleton is called"
        if cls not in cls._instance:
            cls._instance[cls]= super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class myclass():
    __metaclass__ = Singleton
   
    def __init__(self, name=None):
        print"Initialiser is called"
        self.name = name

obj1 = myclass('Brijesh')
obj2 = myclass('Chaudhary')
print"obj address:",obj1, obj2
print"name:",obj1.name, obj2.name 
