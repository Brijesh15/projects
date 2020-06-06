import requests
import json
import traceback
import os, sys
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from ..configParser.readConfig import Config
#import xml.etree.ElementTree as ET
from retry_requests import retry
from requests import Session
path = os.path.dirname(os.path.abspath(__file__)).split('requestRemote')[0]

class request_remote():

    def req(self, url, payload, timeout=300):
        """
        """
        try:
            resp = requests.post(url, data=json.dumps(payload), headers={"content-type": "application/json"}, timeout=timeout)
            return resp
        except:
            print("Error occurred in request_remote",traceback.format_exc())
            return False

    def get_IPPort(self, node_name):

        filePath = path +'/configuration/interfaceConfig.yaml'
        conf = Config(filePath)
        confDict = conf.get_node_data('systemConfigurationin')
        ip = confDict.get(node_name).get('ip')
        port = confDict.get(node_name).get('port')
        return ip, port

    def req_remote(self, api, path, payload={}, reqServer='udr', headers={"content-type": "application/json"}, timeout=30):

        print("printing from request remote")
        ip_port= self.get_IPPort(reqServer)
        url = "http://" + ip_port[0] + ":" + ip_port[1] + '/' + path
        my_session = retry(Session(), retries=2, backoff_factor=0.2)
        try:
            print("calling node:- payload",payload)
            if api == 'post':
                resp = my_session.post(url, data=json.dumps(payload), headers=headers, timeout=timeout)
            if api == 'put':
                resp = requests.put(url, data=json.dumps(payload), headers=headers, timeout=timeout)
            if api == 'get':
                resp = my_session.get(url, data=json.dumps(payload), headers=headers, timeout=timeout)
            if api == 'patch':
                resp = my_session.patch(url, data=json.dumps(payload), headers=headers, timeout=timeout)
            print("resp", resp)
            #if type(resp.json()) != dict:
            return resp
            #if resp.json().get('error'):
            #    return '{0}'.format(resp.json().get('error'))
            #return '{0}'.format(resp.json().get('status'))
        except requests.exceptions.ConnectionError as e:
            print("ConnectionError occurred in request_remote",e)
            return Response({"title" :"NETWORK_FAILURE" , "cause" : "ConnectionError occurred while making connection to other node"}, \
                            content_type="application/json", status=status.HTTP_504_GATEWAY_TIMEOUT)
        except:
            print("Error occurred in request_remote",traceback.format_exc())
            #return Response({"ddd":"brijesh"}, content_type="application/json", status=status.HTTP_504_GATEWAY_TIMEOUT)
            return False




