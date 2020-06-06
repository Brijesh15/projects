import threading
class X:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.RLock()
        #self.lock = threading.Lock()

    def changeA(self):
        with self.lock:
#        if self.lock:
            self.a = self.a + 1
#            print"a:",self.a
            return self.a 

    def changeB(self):
        with self.lock:
#        if self.lock:
            self.b = self.b + self.a
#            print"b:",self.b
            return self.b 

    def changeAandB(self):
        # you can use chanceA and changeB threadsave!
        with self.lock:
#        if self.lock:
            print"A:",self.changeA() # a usual lock would block in here
            print"B:", self.changeB()


X().changeAandB()
