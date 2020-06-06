class singleton():
	instance = None
	
	@classmethod
	def Instance(cls):
		print "Instance invoked"
		if cls.instance ==None:
			cls.instance =singleton()
		return cls.instance

	def __init__(self):
		print "Constructore Invoked"
		if self.instance !=None:
			raise ValueError("A singleton instance is already exist!")

	def Setdata(self,num):
		self.data =num
	def Getdata(self):
		return self.data

#obj= singleton.Instance()
obj= singleton.Instance().Setdata(11)
obj1= singleton()
print ('Data is %s '% (singleton.Instance().Getdata()))
#obj1 = singleton()
