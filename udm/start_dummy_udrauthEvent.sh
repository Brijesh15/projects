#!/bin/bash

message=$(echo '{}')

len=$(echo "$message" | wc -c)

#set -x
while true 
do
	(
	echo -en "HTTP/1.1 204 OK\r\n"
	echo -en "Connection: keep-alive\r\n"
	echo -en "Content-Type: text/html; charset=iso-8859-1\r\n"
	echo -en "Content-Length: $len\r\n\r\n"
	echo -e "$message"
	#sleep 5 #To test behavior of slow UDM uncomment this line
	) 
done | nc -k -l 127.0.0.1 8005

