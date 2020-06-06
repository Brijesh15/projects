class parent:
		
	def display(self):
		print "employee no:%d"% self.count ,"name :", self.name, "Salary:",self.salary,"\n" 

class child(parent):
	count=0
	def __init__(self,name,salary):
		print "child constructor invoked"
		self.salary=salary
		self.name=name
		child.count+=1

	def childdetail(self):
		self.display()

#c=child("karan",20000)
#child("karan",2000).display()
d=child("Rohan",30000)
d.childdetail()		
