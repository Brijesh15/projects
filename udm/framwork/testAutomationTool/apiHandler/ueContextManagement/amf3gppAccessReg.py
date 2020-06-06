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


class amf3gppAccessRegistraion(APIView):

    def get(self, request, ueId):

        try:
            from ...validator.amf3gppAccessRegValidator import amf3gppAccessRegValidator
            supportedFeatures = request.GET.get("supportedFeatures")
            req = request_remote()
            if supportedFeatures :
                res = req.req_remote("get", "subscription-data/%s/context-data/amf-3gpp-access/?supportedFeatures=%s"
                                     %(ueId, supportedFeatures))
            else:
                res = req.req_remote("get", "subscription-data/%s/context-data/amf-3gpp-access/"%(ueId))
            if res.status_code != 200:
                return res
            amf3gpp = res.json()
            logger.info("amf3gpp %s"%(amf3gpp))
            amf3gppValid = amf3gppAccessRegValidator(data=amf3gpp)
            if not amf3gppValid.is_valid():
                logger.error("amf3gpp validation error %s"%(amf3gppValid.errors))
                json_res = {"title": "amf3gpp parameters didn't validate", "status": 502, \
                             "invalidParams": amf3gppValid.errors, "supportedFeatures": request.GET.get("supportedFeatures", "")}
                return Response(json_res, content_type="application/json", status=status.HTTP_502_BAD_GATEWAY)
            return HttpResponse(json.dumps(amf3gpp), content_type="application/json")
        except:
            logger.error("exception %s"%(traceback.format_exc()))
            json_res = {"title": "error occurred while amf3gppAccessRegistraion information", "status": 500, \
                        "supportedFeatures": request.GET.get("supportedFeatures", "")}
            return HttpResponseServerError(json.dumps(json_res), content_type="application/json")


if __name__ == "__main__":

    pass
