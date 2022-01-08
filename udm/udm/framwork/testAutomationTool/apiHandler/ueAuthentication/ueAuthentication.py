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
from ctypes import *
import random
import hashlib
import hmac
from ...configParser.readConfig import Config
from ...requestRemote.request_remote import request_remote
path = os.path.dirname(os.path.abspath(__file__)).split('apiHandler')[0]
from ...projectLogging.xglogging import get_xglogger
logger = get_xglogger()


class derivAuVector():

    @staticmethod
    def fillhexValue(key, hexString):

        hexlist = []
        j = 0
#        print("printing hex value")
        for i in range(0,len(hexString),2):
              key[j] = int("0x"+hexString[i:i+2], 16)
              j+=1

    @staticmethod
    def genrandomHex():
        conf = Config(path +"configuration/interfaceConfig.yaml")
        confDict = conf.get_all_data()
        if confDict.get('isUtRun'):
            return "a3b1e4799fcd3dadc055b7db51497f9d"
        hex_out = ""
        hex_char = '0123456789abcdef'
        hex_sample = [random.choice(hex_char) for _ in range(32)]
        hex_out = "".join(hex_sample)
        return hex_out

    @staticmethod
    def convertHexStr(hexlist):
        hexStr = ""
        for i in hexlist:
            #hexStr+="%02x"%hex(i).replace("0x","")
            hexStr+="%02x"%int(i)
        print(hexStr)
        return hexStr

    @staticmethod
    def HMAC_SHA256(key, S):
        message = bytes(S, 'utf-8')
        secret = bytes(key, 'utf-8')
        signature = hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()
        print(signature)
        return signature

    def decodeSupi(self, suci):
        return suci

    def genAutn(self, SQN, AK, AMF, MAC):
        """
        this function deriv the AUTN
        """
        sqn = self.convertHexStr(SQN)
        ak = self.convertHexStr(AK)
        mac = self.convertHexStr(MAC)
        print(type(ak))
        print("autn val",sqn, ak, AMF, mac)
        #autn = hex(int(int(sqn, 16) ^ int(ak, 16))) + AMF + mac
        autn = "%012x"%int(int(sqn, 16) ^ int(ak, 16)) + AMF + mac
        autn = autn.replace("0x","")
        print("autn len",len(autn), autn)
        return autn

    def derivKausf(self, CK, IK, servingNetworkName, SQN, AK):
        """
        this function deriv the Kausf
        """
        ck = self.convertHexStr(CK)
        ik = self.convertHexStr(IK)
        sqn = self.convertHexStr(SQN)
        ak = self.convertHexStr(AK)
        FC = "6a"
        P0 = servingNetworkName
        L0 = "%04x"%int(len(servingNetworkName))
        P1 = hex(int(int(sqn, 16) ^ int(ak, 16))).replace("0x","")
        L1 = "0006"
        print("P0 L0, P1, L1 =", P0,L0,P1,L1)
        S = FC + P0 + L0 + P1 + L1
        key = ck + ik
        return self.HMAC_SHA256(key, S)

    def derivXresStar(self, CK, IK, servingNetworkName, RAND, XRES):
        """
        this function deriv the Xres*
        """
        ck = self.convertHexStr(CK)
        ik = self.convertHexStr(IK)
        rand = self.convertHexStr(RAND)
        xres = self.convertHexStr(XRES)
        FC = "6b"
        P0 = servingNetworkName
        L0 = "%04x"%int(len(servingNetworkName))
        P1 = rand
        L1 = "0010"
        P2 = xres
        xresLen = len(xres)
        L2 = "%04x"%int(xresLen/2)
        print("P0 L0, P1, L1 P2 L2=", P0,L0,P1,L1,P2, L2)
        S = FC + P0 + L0 + P1 + L1 + P2 + L2
        key = ck + ik
        return self.HMAC_SHA256(key, S)[32:]

    def fiveGaka(self, supi, args, authSub):

        servingNetworkName = args.get("servingNetworkName")
        ausfInstanceId = args.get("ausfInstanceId")
        fun = CDLL(path + "/apiHandler/ueAuthentication/libfun.so")
        fun1 = fun.f1
        fun2345 = fun.f2345
        fun1.argtypes = POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)
        fun2345.argtypes = POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8), POINTER(c_uint8)
        K = (c_uint8 * 16)()
        RAND = (c_uint8 * 16)()
        SQN = (c_uint8 * 6)()
        AMF = (c_uint8 * 2)()
        MAC = (c_uint8 * 8)()
        XRES = (c_uint8 * 8)()
        CK = (c_uint8 * 16)()
        IK = (c_uint8 * 16)()
        AK = (c_uint8 * 6)()
        self.fillhexValue(K, authSub.get("encPermanentKey"))
        self.fillhexValue(RAND, self.genrandomHex())
        self.fillhexValue(SQN, authSub.get("sequenceNumber").get("sqn"))
        self.fillhexValue(AMF, authSub.get("authenticationManagementField"))
        logger.info("K %s, RAND %s, SQN %s, AMF %s"%(K, RAND, SQN, AMF))
        fun1(K, RAND, SQN, AMF, MAC)
        fun2345(K, RAND, XRES, CK, IK, AK)
        print("SQN %s AK %s"%(SQN, AK))
        logger.info("XRES %s"%(list(XRES)))
        AUTN = self.genAutn(SQN, AK, authSub.get("authenticationManagementField"), MAC)
        Kausf = self.derivKausf(CK, IK, servingNetworkName, SQN, AK)
        logger.info("AUTN %s"%(AUTN))
        logger.info("Kausf %s"%(Kausf))
        XresStar = self.derivXresStar(CK, IK, servingNetworkName, RAND, XRES)
        json_res = {"authType" : "5G_AKA", "supportedFeatures" : "", "authenticationVector" : {"avType" : "5G_HE_AKA",
                    "rand" : self.convertHexStr(RAND), "xresStar": XresStar, "autn" : AUTN, "kausf": Kausf}, "supi" : supi}
        return HttpResponse(json.dumps(json_res), content_type="application/json")

class generateAuthData(APIView, derivAuVector):

    def post(self, request, supiOrSuci):

        try:
            from ...validator.ueAuthValidator import generateAuthValidator, authSubscriptionValidator
            args = request.data
            logger.info("request args %s supiOrSuci %s"%(request.data, supiOrSuci))
            auth = generateAuthValidator(data=args)
            if not auth.is_valid():
                logger.error("auth validation error %s"%(auth.errors))
                json_res = {"title": "request parameters didn't validate", "status": 400, \
                             "invalidParams": auth.errors, "supportedFeatures": args.get("supportedFeatures", "")}
                return HttpResponseBadRequest(json.dumps(json_res), content_type="application/problem+json")
            req = request_remote()
            supi = self.decodeSupi(supiOrSuci)
            res = req.req_remote("get", "subscription-data/%s/authentication-data/authentication-subscription/"%(supi))
            if res.status_code != 200:
                return res
            authSub = res.json()
            logger.info("auth sub %s"%(authSub))
            authValid = authSubscriptionValidator(data=authSub)
            if not authValid.is_valid():
                logger.error("auth sub validation error %s"%(authValid.errors))
                json_res = {"title": "auth subscription parameters didn't validate", "status": 502, \
                             "invalidParams": authValid.errors, "supportedFeatures": args.get("supportedFeatures", "")}
                return Response(json_res, content_type="application/json", status=status.HTTP_502_BAD_GATEWAY)
            if authSub.get("authenticationMethod") == "5G_AKA":
                return self.fiveGaka(supi, args, authSub)
            json_res = {"title": "this authentication method is not implemented", "status": 501, \
                        "supportedFeatures": args.get("supportedFeatures", "")}
            return Response(json_res, content_type="application/json", status=status.HTTP_501_NOT_IMPLEMENTED)
        except:
            logger.error("exception %s"%(traceback.format_exc()))
            json_res = {"title": "error occurred while getting authentication vector created successfully", "status": 500}
            return HttpResponseServerError(json.dumps(json_res), content_type="application/json")


class authEvents(APIView):

    def post(self, request, supi):

        try:
            from ...validator.ueAuthValidator import authEvents
            args = request.data
            logger.info("request args %s supi %s"%(request.data, supi))
            authconfirm = authEvents(data=args)
            logger.debug("authconfirm %s"%(authconfirm))
            if not authconfirm.is_valid():
                logger.error("authconfirm validation error %s"%(authconfirm.errors))
                json_res = {"title": "auth events parameters didn't validate", "status": 400, \
                             "invalidParams": authconfirm.errors, "supportedFeatures": args.get("supportedFeatures", "")}
                return HttpResponseBadRequest(json.dumps(json_res), content_type="application/problem+json")
            req = request_remote()
            res = req.req_remote("put", "nudm-ueau/v1/%s/auth-events"%(supi))
            if res.status_code != 204:
                return res
            return Response(args, content_type="application/json", status=status.HTTP_201_CREATED)
        except:
            print("try error",traceback.format_exc())
            logger.error("exception %s"%(traceback.format_exc()))
            json_res = {"title": "error occurred while getting authentication confimation", "status": 500}
            return HttpResponseServerError(json.dumps(json_res), content_type="application/json")




if __name__ == "__main__":

    pass
