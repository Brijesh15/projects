from .commDatabase import database
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError, HttpResponseNotFound,                                 HttpResponseServerError
from  rest_framework.views import APIView
from django.db import connections
import json
import time

class company(APIView):

    def get(self, request):

        try:
            db=database()
            data = db.get_raw_query("select * from company_list;")
            print(data)
            if not data:
                json_res = {"success" : False, "message": "There are no companies details in the database"}
                return HttpResponse(json.dumps(json_res), content_type="application/json")
            json_res = {"success" : True, "items":  [{'id':t[0], 'name': t[1]} for t in data]}
            return HttpResponse(json.dumps(json_res), content_type="application/json")
        except:
            json_res = {"success" : False, "message": "error occurred while getting companies list"}
            return HttpResponse(json.dumps(json_res), content_type="application/json")

    #def post(self, request):

    #    args = request.data
    #    print("args: %s"%args)
    #    db=database()
    #    check_cmd = "select * from company_list where company_name='%s'"%(args.get('company_name'))
    #    res = db.check_interies(check_cmd)
    #    if res:
    #        return HttpResponse("<h2> Company details already inserted </h2>")

    #    cmd = "insert into company_list (company_name) values ('%s')"%(args.get('company_name'))
    #    print("cmd: %s"%cmd)
    #    db.insert_data(cmd)
    #    return HttpResponse("<h2> Insert company details successfully </h2>")

class checkQrcode(APIView):

    def put(self, request, company_id):

        args = request.data
        print("args: %s"%args)
        db=database()
        qr = args.get('qr')
#        cmd = "select scanned_result from company_qrcode where company_id=%s and qrcode='%s'"%(company_id, qr)
#        flag = db.get_raw_query(cmd)
#        print(flag)
#        if not flag:
#            return HttpResponse(json.dumps({"success" : False, "message": "Qrcode not inserted in the database"}),
#                                content_type="application/json")

#        if flag[0][0] == 'not scanned':
            #print(res[0])
#            cmd = "update company_qrcode set scanned_result='scanned', updated_at='%s' where company_id=%s and \
#            qrcode='%s'"%(time.time(), company_id, qr)
#            db.insert_data(cmd)
#            return HttpResponse(json.dumps({"success" : True}), content_type="application/json")
#        return HttpResponse(json.dumps({"success": False , "message": "Qrcode already used"}), content_type="application/json")

        company_name = db.get_data('company_name', 'company_list', 'company_id', company_id)[0]
        cmd = "select scanned_result from %s where qrcode='%s'"%(company_name, qr)
        flag = db.get_raw_query(cmd)
        print(flag)
        if not flag:
            return HttpResponse(json.dumps({"success" : False, "message": "QR not inserted in the database"}),
                                content_type="application/json")

        if flag[0][0] == 'not scanned':
            #print(res[0])
            cmd = "update %s set scanned_result='scanned', updated_at='%s' where qrcode='%s'"%(company_name, time.time(), qr)
            db.insert_data(cmd)
            return HttpResponse(json.dumps({"success" : True}), content_type="application/json")
        return HttpResponse(json.dumps({"success": False , "message": "QR already used"}), content_type="application/json")

