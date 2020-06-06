from multiprocessing import Process , Lock
import os, time

def lock(n,l):
	l.acquire()
#	time.sleep(1)
	print "NUMBER:{0} and PID: {1}".format(n,os.getpid())
	l.release()

if __name__ == '__main__':
	L = Lock()
	for n in range(10):
		P = Process(target = lock , args=(n,L,))		
		P.start()
		P.join()
#		P.run()
