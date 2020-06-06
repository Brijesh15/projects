class Kls(object):
    no_inst = 5

    def __init__(self):
        self.no_inst = self.no_inst + 1

    @classmethod
    def get_no_of_instance(cls):
        cls.no_inst +=1
        return cls.no_inst

ik1 = Kls()
ik2 = Kls()
print ik1.no_inst
print ik2.no_inst
print ik1.get_no_of_instance()
print ik2.get_no_of_instance()
print Kls.get_no_of_instance()
ik3 = Kls()
print ik3.no_inst

