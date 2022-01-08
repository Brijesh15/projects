class A:
    def __init__(self):
        self._i = 1
        self.j = 5
        self.__k = 4
    def display(self):
        print(self._i, self.j, self.__k)

class B(A):
    def __init__(self):
        super().__init__()
        self._i = 2
        self.j = 7
        self.__k = 6

c = B()
c.display()
