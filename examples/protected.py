#import pdb

class A():

    __num = 0
    _number = 1
    def __init__(self,args):
        self.__num = args
        print "self._num",self.__num
#        self.__update(30)

    def __update(self, num):
        self.__num = num
        print "self._num",self.__num
    
class B(A):
    
    def __init__(self):
        #self.__update(15) 
        pass
#        print"__num",self.__num

a = A(10)
obj = B()
#obj.__update(20)
#print"obj._number", obj._number
#print"obj.__num", obj.__num
#print"obj._B__num", obj._A__num
