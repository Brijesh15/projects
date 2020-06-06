from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
import traceback
from  rest_framework.views import APIView
import json, os
path = os.path.dirname(os.path.abspath(__file__))
from .testAutomationTool.projectLogging.xglogging import createJsonLogging
logger = createJsonLogging('xg1Klogger', path + '/testAutomationTool/projectLogging/amantya.log')

"""
class systemStartOP(APIView):

    def get(self, request):

        try:
            logger = createJsonLogging('xg1Klogger', path + '/testAutomationTool/projectLogging/amantya.log')
            json_res = {"title": "default operation during system start is started successfully", "status": 200}
            logger.info("default operation during system start is started successfully")
            return HttpResponse(json.dumps(json_res), content_type="application/json")
        except:
            json_res = {"title": "error occurred while starting default operation", "status": 500}
            logger.error("error occurred while starting default operation")
            return HttpResponseServerError(json.dumps(json_res), content_type="application/json")
"""
