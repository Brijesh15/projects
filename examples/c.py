from datetime import date 
  
class Person: 
    def __init__(self, name, age, no=''): 
        print"initialiser called"
        self.name = name 
        self.age = age 
        self.no = no
 
    # a class method to create a Person object by birth year. 
    @classmethod
    def fromBirthYear(cls, name, year): 
        print"class method called"
        return cls(name, date.today().year - year, 83) 
      
    # a static method to check if a Person is adult or not. 
    @staticmethod
    def isAdult(age): 
        return age > 18
  
#person1 = Person('mayank', 21) 
#person3 = Person('mayankfgfg', 20) 
person2 = Person.fromBirthYear('brijesh', 1994) 
  
#print person1.name
#print person3.name
print person2.no
  
# print the result 
print Person.isAdult(22) 
