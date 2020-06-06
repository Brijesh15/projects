from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseNotFound, \
        HttpResponseBadRequest, HttpResponseForbidden
from rest_framework import status
from rest_framework.response import Response
from  rest_framework.views import APIView
from django.db import connections
import json, os
import time
import ctypes
import traceback
from ...requestRemote.request_remote import request_remote
path = os.path.dirname(os.path.abspath(__file__)).split('apiHandler')[0]
from ...projectLogging.xglogging import get_xglogger
logger = get_xglogger()


class accessAndMobility(APIView):

    def get(self, request, supi):

        try:
            from ...validator.amDataValidator import accessAndMobilityValidator
            supportedFeatures = request.GET.get("supportedFeatures")
            plmnId = request.GET.get("plmnId")
            req = request_remote()
            ueId = supi
            if supportedFeatures :
                res = req.req_remote("get", "/subscription-data/%s/%s/provisioned-data/am-data/?supportedFeatures=%s"
                                     %(ueId, plmnId, supportedFeatures))
            else:
                res = req.req_remote("get", "/subscription-data/%s/%s/provisioned-data/am-data/"%(ueId, plmnId))
            if res.status_code != 200:
                return res
            amData = res.json()
            logger.info("amData %s"%(amData))
            amValid = accessAndMobilityValidator(data=amData)
            if not amValid.is_valid():
                logger.error("Access and Mobilit data validation error %s"%(amValid.errors))
                json_res = {"title": "Access and Mobilit data didn't validate", "status": 502, \
                             "invalidParams": amValid.errors, "supportedFeatures": request.GET.get("supportedFeatures", "")}
                return Response(json_res, content_type="application/json", status=status.HTTP_502_BAD_GATEWAY)
            return HttpResponse(json.dumps(amData), content_type="application/json")
        except:
            logger.error("exception %s"%(traceback.format_exc()))
            json_res = {"title": "error occurred while getting Access and Mobilit information", "status": 500, \
                        "supportedFeatures": request.GET.get("supportedFeatures", "")}
            return HttpResponseServerError(json.dumps(json_res), content_type="application/json")


if __name__ == "__main__":

    pass
