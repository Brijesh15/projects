from multiprocessing import Process, RLock, BoundedSemaphore
import os, time
 
def brijesh(arg):
        print "waiting for releasing lock"
        l.acquire()
	print arg
	print 'module_name:',__name__
	if hasattr(os,'getppid'):
		print "parent process:",os.getppid()
	print 'Process id:',os.getpid()
        l.release()

def HI(name,l):
	#brijesh('function Hi')
        print "waiting for acquiring lock1"
        l.acquire()
	brijesh('function Hi')
	print 'Hi starting'
        print "parent process:",os.getppid()
	print 'Process id:',os.getpid()
        start = time.time()
        #time.sleep(5)
        while (time.time() - start) < 0.01:
	    print 'Hello',name
        l.release()
        
if __name__ == '__main__':
	#brijesh('main line1')
	#HI('main line2')
        l = BoundedSemaphore(2)
        #l = RLock()
	p=Process(target=HI, args=('bob',l,))
	p1=Process(target=HI, args=('Brijesh chaudhary',l,))
	p.start()
        print "waiting for acquiring lock2"
        l.acquire()
        time.sleep(2)
        l.release()
	#p.join()	
	#brijesh('main line1')
	#p1.start()
	#p1.join()	
	print 'Done'

#main line
#module_name: __main__
#parent process: 13932
#Process id: 501
#function Hi
#module_name: __main__
#parent process: 501
#Process id: 502
#Hello bob
