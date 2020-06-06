from .commDatabase import database
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseNotFound,                                 HttpResponseServerError
from  rest_framework.views import APIView
from ..models import *
from django.db import connections
import json
import time

class company(APIView):

    def get(self, request):

        try:
            #db=database()
            #data = db.get_raw_query("select * from company_list;")
            data = company_list.objects.all().values()
            print(data)
            if not data:
                json_res = {"success" : False, "message": "There are no companies details in the database"}
                return HttpResponse(json.dumps(json_res), content_type="application/json")
            #json_res = {"success" : True, "items":  [{'id':t[0], 'name': t[1]} for t in data]}
            json_res = {"success" : True, "items":  [{'id':t.get("company_id"), 'name': t.get("company_name")} for t in data]}
            return HttpResponse(json.dumps(json_res), content_type="application/json")
        except:
            json_res = {"success" : False, "message": "error occurred while getting companies list"}
            return HttpResponse(json.dumps(json_res), content_type="application/json")


class checkQrcode(APIView):

    def put(self, request, company_id):

        args = request.data
        print("args: %s"%args)
        #db=database()
        qr = args.get('qr')
        company_name = company_list.objects.filter(company_id=company_id).values()[0]["company_name"]
        #company_name = db.get_data('company_name', 'company_list', 'company_id', company_id)[0]
        #qrField = 'qrcode'
        if company_name.lower() == "Airtel".lower() and args.get('vpa'):
            #qrField = 'vpa'
            flag = PhonePe.objects.filter(vpa=qr).values()
        else:
        #cmd = "select scanned_result from %s where %s='%s'"%(company_name, qrField, qr)
        #flag = db.get_raw_query(cmd)
            flag = PhonePe.objects.filter(qrcode=qr).values()
        print(flag)
        if not flag:
            return HttpResponse(json.dumps({"success" : False, "message": "QR not inserted in the database"}),
                                content_type="application/json")

        if flag[0].get("scanned_result") == 'not scanned':
            #cmd = "update %s set scanned_result='scanned', updated_at='%s' where %s='%s'"%(company_name, time.time(), qrField, qr)
            #db.insert_data(cmd)
            updateStatus = PhonePe.objects.get(qrcode=qr)
            updateStatus.scanned_result = 'scanned'
            updateStatus.save()
            return HttpResponse(json.dumps({"success" : True}), content_type="application/json")
        return HttpResponse(json.dumps({"success": False , "message": "QR already used"}), content_type="application/json")
