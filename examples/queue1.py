from multiprocessing import Process , Queue

def put_queue(q):
	lst = [1,3,2,5,10,8]
	for item in lst:
		q.put(item)


if __name__ == '__main__':
	que = Queue()
	P = Process(target = put_queue, args=(que,))
	P.start()
	for item in range(6):
		print que.get()
	P.join()
