from setting import fic_dict
from client import requesrRemote

def addDynamicFun(cls, name, funName, *args, **kwargs):
    def innerfun(self,*args, **kwargs):
        print"inner1"    
        return funName(cls.__name__, name, *args, **kwargs)
    innerfun.__name__ ="%s"%name 
    setattr(cls, innerfun.__name__,innerfun) 
    print"inner2",innerfun.__name__    

class dynamicClass():

    def __init__(self):
        pass
  
    def create(self, className):
        
        #dyn_class = type(className, (), fic_dict[className])
        self.reqObj = requesrRemote()  
        dyn_class = type(className, (), {})
        for fuc_name in fic_dict[className]:
            addDynamicFun(dyn_class, fuc_name, self.reqObj.reqRemote)  	
        return dyn_class

