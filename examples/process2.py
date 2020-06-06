from multiprocessing import Process
import time,os

def child_p():
	print "Child process begging",os.getpid()
	time.sleep(2)
	print "Child process end"

def Parent_p():
	print "Parent process begging",os.getpid()
	time.sleep(1)
	print "Parent process end"

if __name__ == '__main__':
	print "sub ka BAAP process begging",os.getpid()
	c = Process(name='chlid_1',target=child_p)
	p = Process(name='Parent_1',target=Parent_p)

	c.start()
	#c.join()
	p.start()
	#p.join()
        #for i in range(2):
	#    p.start()
	#    p.join()
        #    print"PID -is %s"%p.pid
            #os.system('kill -9 %s'% p.pid)
            #os.system('kill -9 11935')
