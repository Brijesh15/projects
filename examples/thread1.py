import threading
import time

class myThread(threading.Thread):
	def __init__(self,threadId,threadName,counter):
		threading.Thread.__init__(self)
		self.threadId=threadId
		self.threadName=threadName
		self.counter=counter
	def run(self):
		print "starting :",self.threadName
		thread_time(self,self.threadName,self.counter,5)
		print "exeting :",self.threadName

def thread_time(self,name,delay,counter):
	while counter:
#		time.sleep(delay)
		print "%s :%s"%(name, time.ctime(time.time()))
		counter-=1


thread1=myThread(1,'Thread:1',2)
thread2=myThread(2,'Thread:2',3)

thread1.start()
thread2.start()

print "Exiting Main thread"
