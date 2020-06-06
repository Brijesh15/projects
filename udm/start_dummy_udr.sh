#!/bin/bash

message=$(echo '{
			"encPermanentKey": "5f1d289c5d354d0a140c2548f5f3e3ba",
			"protectionParameterId": "232a",
			"authenticationMethod": "5G_AKA",
			    "sequenceNumber": {
			    "sqnScheme" : "NON_TIME_BASED",
			    "sqn": "a12bf1234566",
			    "lastIndexes": 1,
			    "indLength": 1,
			    "difsign": "POSITIVE"
		     },
			"authenticationManagementField": "8101",
	    "algorithumId": "1657",
	    "encOpkey": "5f1d289c5d354d0a140c2548f5f3e3ba",
	    "encTopkey": "465b5ce8b199b49faa5f0a2ee238a6bc"		
		}')
len=$(echo "$message" | wc -c)

#set -x
while true 
do
	(
	echo -en "HTTP/1.1 200 OK\r\n"
	echo -en "Connection: keep-alive\r\n"
	echo -en "Content-Type: text/html; charset=iso-8859-1\r\n"
	echo -en "Content-Length: $len\r\n\r\n"
	echo -e "$message"
	#sleep 5 #To test behavior of slow UDM uncomment this line
	) 
done | nc -k -l 127.0.0.1 8005

