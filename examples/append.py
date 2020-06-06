with open("text.txt",'a') as f:

        f1=open("text1.txt" , 'r')
	data=f1.read()
	f.write(data)

