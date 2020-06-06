dd= "AT+CGMR;AT+CGACT=1,2;AT+CGMM;AT+CFUN=1,1"
ss=dd.split(";")
print "bfhbf",ss
for s in ss:
	print"s=", s
	if s == 'AT+CGMR' or s== 'AT+CGMM':
		print"Hi" 
