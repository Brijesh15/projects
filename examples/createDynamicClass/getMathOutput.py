from dynamicClass import dynamicClass


class mathOutput():

    def __init__(self):
        pass

    def executeMathfuc(self):
       
        dynamicObj = dynamicClass()
        mathlibrary = dynamicObj.create('mathClass')
        m= mathlibrary()
        print "addition: ",m.mul(10, 11)             

 
obj = mathOutput()
obj.executeMathfuc()
