from multiprocessing import Process ,Pipe

def pipe(pi):
#	lst = [1,4,'a','g','k']
	dct = {'a':1,'b':2,'c':4,'d':10}
	dc = ()
	tpl = dct.items()
	print tpl
	for key in tpl:
		print'key', key
		dc= dc + key
	pi.send(dc)
	pi.close()

if __name__ == '__main__':
	p_parent , p_child = Pipe()
	P = Process(target = pipe , args=(p_parent,))
	P.start()
	print p_child.recv()
	P.join()
	p_child.close()
	
