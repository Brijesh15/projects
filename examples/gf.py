class human:
	def __init__(man, name=None):
		print man
		man.name=name
 	def speaks(man1):
		print man1.name

	@classmethod
	def raise_amount(cls, amount):
		cls.amount=amount
	@staticmethod
	def isweekday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True


#man=human('Ram')
#woman=human('Rani')
#man.speaks()
#woman.speaks()
import datetime
day=datetime.date(2017, 12 ,9)
print human.isweekday(day)
human.raise_amount(100)
print human.amount
