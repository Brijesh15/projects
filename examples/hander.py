import os , time
from handlr1 import DEF

class ABC(DEF):

	def __init__(self):
	#	self.a = DEF()
		pass

	def func(self,handr,handl,l=None):
		if l:
			lst = handr(l)
		else:
			lst = handl(l)		

	def handlr(self,l):
		print 'Handler: {0}'.format(l)

	def function(self):
		lst = [1,2,3,4,5,6]
		self.func(self.hand,self.handlr,lst)

a = ABC()
a.function()
