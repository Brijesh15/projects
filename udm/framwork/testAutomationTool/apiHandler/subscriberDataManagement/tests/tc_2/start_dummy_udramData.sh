#!/bin/bash

#				"gpsis": [                                                                                                    
#		            1                                                                                                     
#		             ],
message=$(echo '{                                                                                                               
        "supportedFeatures": "123abc50",                                                                              
        "internalGroupIds": [                                                                                         
                  "12345678-123-34-42"                                                                                 
                            ],                                                                                                      
				"subscribedUeAmbr": {                                                                                         
				       "uplink": "12.50Kbps",                                                                                
				       "downlink": "12.50Kbps"                                                                               
			                      },                                                                                                      
			  "nssai": {                                                                                                    
			         "supportedFeatures": "123afbcd",                                                                      
				       "defaultSingleNssais": [                                                                              
				       {                                                                                           
				          "sst": 0,                                                                       
				          "sd": "a123df"                                                                  
				       }                                                                                 
				            ],                                                                                            
              "singleNssais": [                                                                                     
               {                                                                                           
                  "sst": 0,                                                                       
	                "sd": "123abc"                                                                  
	              }                                                                                 
                              ]                                                                                             
              },                                                                                                      
         "ratRestrictions": [ 
				        "NR",
								"string"
								],
				"forbiddenAreas": [                                                                                           
                  {"tacs": ["12af"], "areaCode": "string"},                                                             
                  {"tacs": ["12af"], "areaCode": "string"}                                                              
                 ],                                                                                                      
        "serviceAreaRestriction": {                                                                                   
        "restrictionType": "ALLOWED_AREAS",                                                                   
        "areas": [                                                                                            
            {"tacs": ["12ad"], "areaCode": "string"},                                                        
            {"tacs": ["1daf"], "areaCode": "string"}                                                         
                 ],                                                                                            
        "maxNumOfTAs": 0,                                                                                     
        "maxNumOfTAsForNotAllowedAreas": 0                                                                    
           },                                                                                                      
        "coreNetworkTypeRestrictions": [                                                                              
               "5GC",                                                                                                
               "EPC"                                                                                                 
                ],                                                                                                      
        "rfspIndex": 0,                                                                                               
        "subsRegTimer": 0,                                                                                            
        "ueUsageType": 0,                                                                                             
        "mpsPriority": true,
        "mcsPriority": true,                                                                                              
        "activeTime": 0,                                                                                                
        "dlPacketCount": 0,                                                                                           
        "sorInfo": {                                                                                                
               "ackInd": true,                                                                                     
               "sorMacIausf": "string",                                                                            
               "countersor": "string",                                                                             
               "provisioningTime": "2020-03-31T11:39:31.289Z"                                                      
                   },                                                                                                    
               "upuInfo": {                                                                                              
               "upuDataList": [                                                                                  
                   null,                                                                                   
                   null                                                                                    
                              ],                                                                                        
               "upuRegInd": true,                                                                                
               "upuAckInd": true,                                                                                
               "upuMacIausf": "string",                                                                          
               "counterUpu": "string",                                                                           
               "provisioningTime": "2020-03-31T11:39:31.289Z"                                                    
                },                                                                                                  
               "micoAllowed": true,                                                                                    
               "sharedAmDataIds": [                                                                                  
               "12345-."                                                                                     
                  ],                                                                                              
               "subscribedDnnList": [                                                                              
               "string",                                                                                   
               "string"                                                                                    
                      ],                                                                                            
               "nssaiInclusionAllowed": false                                                                    
 } ')

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

