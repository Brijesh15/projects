from multiprocessing import Process , current_process
import time

def daemon():
	p = current_process()
	print"starting daemon process",p.name
	time.sleep(1)
	print"Exiting daemon process",p.name
def non_daemon():
	p = current_process()
	print"starting non daemon process",p.name
	time.sleep(1)
	print"Exiting non daemon process",p.name

if __name__ == "__main__":
	D = Process(target=daemon,name='brijesh')
	D.daemon = True
	N = Process(target=non_daemon,name='Brijesh')
	N.daemon = False
	D.start()
	N.start()
#	D.join()
#	N.join()
	
