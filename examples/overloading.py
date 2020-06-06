#overriding Method
class Parent:        # define parent class
   def myMethod(self):
      print 'Calling parent method'

class Child(Parent): # define child class
   def myMethod(self):
      print 'Calling child method'
c = Child()          # instance of child
c.myMethod()         # child calls overridden method

#operator overloading
class Vector:
	def __init__(self, a, b):
		self.a = a
      		self.b = b

#	def __str__(self):
#      		return 'Vector (%d,%d)' % (self.a,self.b)
   
   	def __pow__(self,other):
		a= self.a ** other.a
		b= self.b ** other.b
#		return  Vector(a,b)
		return  (a,b)
#      		return Vector(self.a % other.a, self.b % other.b)

v1 = Vector(2,10)
v2 = Vector(5,2)
print v1 ** v2
print Vector(2,10) ** Vector(4,5)

#datahiding
class counter:
	__seckretno=0
	def count(self):
		self.__seckretno+=1
		print self.__seckretno

c=counter()
c.count()
c.count()
print c.__seckretno
	




 

