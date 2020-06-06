from multiprocessing import Process,Manager

def manegr(d,l):
	d['a'] = 'A'
	d['b'] = 'B'
	d[1] = 10
	l[0] = 1
	l[1] = 2


if __name__ == '__main__':
	manager = Manager()
	D = manager.dict()
	L = manager.list(range(2))
	P = Process(target= manegr, args=(D,L,))
	P.start()
	P.join()
	print D
	print L
