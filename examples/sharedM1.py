from multiprocessing import Process, Value, Array

def shared(n,a):
	n.value = 6
	for i in range(len(a)):
		a[i] = -a[i] + i*i


if __name__ == '__main__':
	num = Value('i',2)
	arr = Array('i',range(3))
	P = Process(target = shared, args=(num,arr,))
	P.start()
	P.join() 
	print "value:",num.value
	print "Array:",arr[:]
