from .commDatabase import database
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from  rest_framework.views import APIView
from django.db import connections
import json
import csv, io
import os
import time
from datetime import datetime
from .readConfig import Config
import traceback
path = os.path.dirname(os.path.abspath(__file__))

class impExpdata(APIView):

    def get(self, request, company_id):

        try:
            db=database()
            company_name = db.get_data('company_name', 'company_list', 'company_id', company_id)[0]
#            data_set = db.get_raw_query("select * from company_qrcode where company_id='%s'"%(company_id))
            data_set = db.get_raw_query("select * from %s;"%(company_name))
            print(data_set)
            if not data_set:
                json_res = {"success" : False, "message": "There are no companies details in the database, please upload first"}
                return HttpResponse(json.dumps(json_res), content_type="application/json")
            up_obj = uploaddownload()
            if company_name == 'PhonePe':
                return up_obj.PhonePeDownload(company_name, data_set)
            elif company_name == 'Airtel':
                return up_obj.AirtelDownload(company_name, data_set)
            #list_res = [{'Company Name':company_name, 'Scanned Result': t[2], 'Qrcode': t[3], \
            #             'Created at':datetime.utcfromtimestamp(t[4]).strftime("%Y-%m-%dT%H:%M:%SZ"), \
            #             'Updated at':datetime.utcfromtimestamp(t[5]).strftime("%Y-%m-%dT%H:%M:%SZ")} \
            #            if t[5] is not None else {'Company Name':company_name, 'Scanned Result': t[2], 'Qrcode': t[3], \
            #                                      'Created at':datetime.utcfromtimestamp(t[4]).strftime("%Y-%m-%dT%H:%M:%SZ"), \
            #                                      'Updated at':t[5]} for t in data_set]

#            list_res = [{'Company Name':company_name, 'Scanned Result': t[2], 'Qrcode': t[3], \
#                         'Created at':datetime.fromtimestamp(t[4]).strftime("%d-%m-%Y %H:%M:%S"), \
#                         'Updated at':datetime.fromtimestamp(t[5]).strftime("%d-%m-%Y %H:%M:%S")} if t[5] is not None \
#                        else {'Company Name':company_name, 'Scanned Result': t[2], 'Qrcode': t[3], \
#                              'Created at':datetime.fromtimestamp(t[4]).strftime("%d-%m-%Y %H:%M:%S"), \
#                              'Updated at':t[5]} for t in data_set]

#            with open(path+'/companyQrcodes.csv', 'w', newline='') as file:
#                fieldnames = ['Company Name', 'Scanned Result', 'Qrcode', 'Created at', 'Updated at']
#                writer = csv.DictWriter(file, fieldnames=fieldnames)
#                writer.writeheader()
#                for item in list_res:
#                    print(item)
#                    writer.writerow(item)
#            cmd= "cp " + path +"/companyQrcodes.csv" + " "+ path + "/companyQrcodes.xlsx"
#            os.system(cmd)
#            with open(path+'/companyQrcodes.xlsx') as myfile:
#                response = HttpResponse(myfile, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
#                response['Content-Disposition'] = 'attachment; filename=companyQrcodes.xlsx'
#                return response
            #with open(path+'/companyQrcodes.csv') as myfile:
            #    response = HttpResponse(myfile, content_type='text/csv')
            #    response['Content-Disposition'] = 'attachment; filename=companyQrcodes.csv'
            #    return response
        except:
            print("exception : %s"%traceback.format_exc())
            json_res = {"success" : False, "message": "error occurred while downloading company Qr codes"}
            return HttpResponse(json.dumps(json_res), content_type="application/json")

    def post(self, request, company_id):

        try:
            print(request.data)
            print("company_id %s"%company_id)
            db=database()
            company_name = db.get_data('company_name', 'company_list', 'company_id', company_id)[0]
            #print(company_name)
            conf = Config(path + "/csvConfig.cfg")
            confDict = conf.get_section_value('UPLOAD_CSV_COLUMN_NO', [company_name])
            print("filelist",request.FILES.getlist('file'))
            filelist = request.FILES.getlist('file')
            #csvfile = request.FILES['file']
#            for csvfile in request.FILES.getlist('file'):
#                print("csvfile",csvfile.name)
#                if not csvfile.name.endswith('.csv'):
#                    json_res = {"success" : False, "message": " Uploaded file %s is not a csv file"%(csvfile.name)}
#                    return HttpResponse(json.dumps(json_res), content_type="application/json")
#
#                data_set = csvfile.read().decode('UTF-8')
#                io_string = io.StringIO(data_set)
#                checkColumn = next(io_string)
#                print(checkColumn, len(checkColumn.split(',')))
#                if len(checkColumn.split(',')) != int(confDict.get(company_name)):
#                    json_res = {"success" : False, "message": "Contents of uploaded csv file format is not supported"}
#                    return HttpResponse(json.dumps(json_res), content_type="application/json")

#                print(io_string)
#                counter=1
#                for column in csv.reader(io_string, delimiter=','):
#                    print("column: %s"%column, len(column))
#                    if len(column) == 0:
#                        counter+=1
#                        continue
                    #if len(column) != confDict.get(company_name):
                    #    json_res = {"success" : False, "message": "Contents of uploaded csv file format is not supported"}
                    #    return HttpResponse(json.dumps(json_res), content_type="application/json")

#                    counter+=1
            up_obj = uploaddownload()
            if company_name.lower() == 'PhonePe'.lower():
                Res = up_obj.PhonePeUpload(db, confDict, company_id, company_name, filelist)
                return Res
            elif(company_name.lower() == 'Airtel'.lower()):
                Res= up_obj.AirtelUpload(db, confDict, company_id, company_name, filelist)
                return Res
            else:
                json_res = {"success" : False, "message": "There are no support for this company"}
                return HttpResponse(json.dumps(json_res), content_type="application/json")
#                    cmd = "select * from company_qrcode where company_id=%s and qrcode='%s'"%(company_id, column[0])
                    #print(cmd)
#                    intry = db.check_interies(cmd)
                    #print(flag)
#                    if intry:
#                        print("%s number qrcode already in the database against this company"%(counter))
#                        json_res = {"success" : False, "message": "%s number qrcode already in the database against this company"%(counter)}
#                        return HttpResponse(json.dumps(json_res), content_type="application/json")
                        #continue
#                    cmd = "insert into company_qrcode (company_id, scanned_result, qrcode, created_at) values \
#                    (%s, 'not scanned','%s', '%s')"%(company_id, column[0], time.time())
                    #print('cmd %s'%cmd)
#                    db.insert_data(cmd)
#                json_res = {"success" : True, "message": "file uploaded successfully"}
#                return HttpResponse(json.dumps(json_res), content_type="application/json")
        except:
            print("exception : %s"%traceback.format_exc())
            json_res = {"success" : False, "message": "error occurred while uploading company Qr codes"}
            return HttpResponse(json.dumps(json_res), content_type="application/json")

class uploaddownload:

    def PhonePeUpload(self, db, confDict, company_id, company_name, filelist):
        print("PhonePe")
        cmd = "select count(*) FROM information_schema.tables WHERE table_schema = 'company' AND table_name = '%s';"%(company_name)
        intry = db.get_raw_query(cmd)
        print("intry",intry[0][0])
        if not intry[0][0]:
            cmd = "CREATE TABLE %s (id INT(11) NOT NULL AUTO_INCREMENT, company_id int, scanned_result varchar(50) , qrid VARCHAR(500), qrcode VARCHAR(500), lot_number varchar(20), created_at int(12), updated_at int(12), PRIMARY KEY (id));"%(company_name)
            db.insert_data(cmd)

        for csvfile in filelist:
            print("csvfile",csvfile.name)
            if not csvfile.name.endswith('.csv'):
                json_res = {"success" : False, "message": " Uploaded file %s is not a csv file"%(csvfile.name)}
                return HttpResponse(json.dumps(json_res), content_type="application/json")

            data_set = csvfile.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            checkColumn = next(io_string)
            print(checkColumn, len(checkColumn.split(',')))
            if len(checkColumn.split(',')) != int(confDict.get('PhonePe')):
                json_res = {"success" : False, "message": "Contents of uploaded csv file %s's format is not supported against this company"%(csvfile.name)}
                return HttpResponse(json.dumps(json_res), content_type="application/json")

            print(io_string)
            counter=1
            for column in csv.reader(io_string, delimiter=','):
                print("column: %s"%column, len(column))
                if len(column) == 0:
                    counter+=1
                    continue

                cmd = "select * from %s where company_id=%s and qrcode='%s'"%(company_name, company_id, column[1])
                #print(cmd)
                intry = db.check_interies(cmd)
                #print(flag)
                if intry:
                    print("%s number qrcode in file %s is already in the database against this company"%(counter, csvfile.name))
                    json_res = {"success" : False, "message": "%s number qrcode in file %s is already in the database against this company"%(counter, csvfile.name)}
                    return HttpResponse(json.dumps(json_res), content_type="application/json")
                    #continue
                print("rfrf",column[2].lstrip('0'))
                cmd = "insert into %s (company_id, scanned_result, qrid, qrcode, lot_number, created_at) values \
                (%s, 'not scanned','%s', '%s', '%s', '%s')"%(company_name, company_id, column[0], column[1], int(column[2].lstrip('0')), time.time())
                print('cmd %s'%cmd)
                db.insert_data(cmd)
        json_res = {"success" : True, "message": "file uploaded successfully"}
        return HttpResponse(json.dumps(json_res), content_type="application/json")

    def PhonePeDownload(self, company_name, data_set):

        print("PhonePe Downloading")
        list_res = [{'Company Name':company_name, 'Scanned Result': t[2], 'QR ID': t[3], 'QR Text': t[4],'Lot Number': t[5], \
                     'Created at':datetime.fromtimestamp(t[6]).strftime("%d-%m-%Y %H:%M:%S"), \
                     'Updated at':datetime.fromtimestamp(t[7]).strftime("%d-%m-%Y %H:%M:%S")} if t[7] is not None \
                    else {'Company Name':company_name, 'Scanned Result': t[2], 'QR ID': t[3], 'QR Text': t[4], \
                        'Lot Number': t[5],'Created at':datetime.fromtimestamp(t[6]).strftime("%d-%m-%Y %H:%M:%S"), \
                        'Updated at':t[7]} for t in data_set]

        with open(path+'/companyQrcodes.csv', 'w', newline='') as file:
            fieldnames = ['Company Name', 'Scanned Result', 'QR ID', 'QR Text', 'Lot Number', 'Created at', 'Updated at']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in list_res:
                print(item)
                writer.writerow(item)
        with open(path+'/companyQrcodes.csv') as myfile:
            response = HttpResponse(myfile, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=companyQrcodes.csv'
            return response

    def AirtelUpload(self, db, confDict, company_id, company_name, filelist):
        print("PhonePe")
        cmd = "select count(*) FROM information_schema.tables WHERE table_schema = 'company' AND table_name = '%s';"%(company_name)
        intry = db.get_raw_query(cmd)
        print("intry",intry[0][0])
        if not intry[0][0]:
            cmd = "CREATE TABLE %s (id INT(11) NOT NULL AUTO_INCREMENT, company_id int, scanned_result varchar(50) , VPA VARCHAR(500), qrcode VARCHAR(500), created_at int(12), updated_at int(12), PRIMARY KEY (id));"%(company_name)
            db.insert_data(cmd)

        for csvfile in filelist:
            print("csvfile",csvfile.name)
            if not csvfile.name.endswith('.csv'):
                json_res = {"success" : False, "message": " Uploaded file %s is not a csv file"%(csvfile.name)}
                return HttpResponse(json.dumps(json_res), content_type="application/json")

            data_set = csvfile.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            checkColumn = next(io_string)
            print(checkColumn, len(checkColumn.split(',')))
            if len(checkColumn.split(',')) != int(confDict.get('Airtel')):
                json_res = {"success" : False, "message": "Contents of uploaded csv file %s's format is not supported against this company"%(csvfile.name)}
                return HttpResponse(json.dumps(json_res), content_type="application/json")

            print(io_string)
            counter=1
            for column in csv.reader(io_string, delimiter=','):
                print("column: %s"%column, len(column))
                if len(column) == 0:
                    counter+=1
                    continue

                cmd = "select * from %s where company_id=%s and VPA='%s' and qrcode='%s'"%(company_name, company_id, column[0], column[1])
                #print(cmd)
                intry = db.check_interies(cmd)
                #print(flag)
                if intry:
                    print("%s number qrcode in file %s is already in the database against this company"%(counter, csvfile.name))
                    json_res = {"success" : False, "message": "%s number qrcode in file %s is already in the database against this company"%(counter, csvfile.name)}
                    return HttpResponse(json.dumps(json_res), content_type="application/json")
                    #continue
                cmd = "insert into %s (company_id, scanned_result, VPA, qrcode, created_at) values \
                (%s, 'not scanned','%s', '%s', '%s')"%(company_name, company_id, column[0], column[1], time.time())
                print('cmd %s'%cmd)
                db.insert_data(cmd)
        json_res = {"success" : True, "message": "file uploaded successfully"}
        return HttpResponse(json.dumps(json_res), content_type="application/json")

    def AirtelDownload(self, company_name, data_set):

        print("Airtel Downloading")
        list_res = [{'Company Name':company_name, 'Scanned Result': t[2], 'VPA': t[3], 'UPI String': t[4], \
                     'Created at':datetime.fromtimestamp(t[5]).strftime("%d-%m-%Y %H:%M:%S"), \
                     'Updated at':datetime.fromtimestamp(t[6]).strftime("%d-%m-%Y %H:%M:%S")} if t[6] is not None \
                    else {'Company Name':company_name, 'Scanned Result': t[2], 'VPA': t[3], 'UPI String': t[4], \
                        'Created at':datetime.fromtimestamp(t[5]).strftime("%d-%m-%Y %H:%M:%S"), \
                        'Updated at':t[6]} for t in data_set]

        with open(path+'/companyQrcodes.csv', 'w', newline='') as file:
            fieldnames = ['Company Name', 'Scanned Result', 'VPA', 'UPI String', 'Created at', 'Updated at']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for item in list_res:
                print(item)
                writer.writerow(item)
        with open(path+'/companyQrcodes.csv') as myfile:
            response = HttpResponse(myfile, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=companyQrcodes.csv'
            return response
