#!/bin/bash

#"amfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",

message=$(echo '{
"supportedFeatures": "12afc430",
"purgeFlag": true,
"pei": "string",
"imsVoPs":"HOMOGENEOUS_SUPPORT",
"deregCallbackUri": "string",
"amfServiceNameDereg" : "nnrf-nfm",
"pcscfRestorationCallbackUri": "string",
"amfServiceNamePcscfRest":"nnrf-nfm",
"initialRegistrationInd": true,
"guami": {
   "plmnId": {
       "mcc": "311",
       "mnc": "480"
             },
       "amfId": "12cfd2"
         },
"backupAmfInfo": [
          {
          "backupAmf": "string",
					"guamiList": [
            {
						 "plmnId": {
						     "mcc": "311",
						     "mnc": "479"
						           },
						  "amfId": "123da0"
						}
						          ]
										        }
										   ],
"drFlag": true,	
"ratType": "NR",
"urrpIndicator": true,
"amfEeSubscriptionId": "string",
"epsInterworkingInfo": {
     "epsIwkPgws": {

     "additionalProp1": {                                                                        
                  "pgwFqdn": "string",                                                            
                  "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"                         
                        },                                                                                
     "additionalProp2": {                                                                        
                  "pgwFqdn": "string",                                                            
                  "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"                         
                        },                                                                                
     "additionalProp3": {                                                                        
                  "pgwFqdn": "string",                                                            
                  "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"                         
                        }                                                                                 
            }                                                                                             
          }                                                                                                       
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

