from rest_framework import serializers

class resynchronization(serializers.Serializer):

    rand = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]*$', max_length=32, min_length=32)
    auts = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]*$', max_length=28, min_length=28)


class generateAuthValidator(serializers.Serializer):

    supportedFeatures = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$')
    servingNetworkName = serializers.RegexField(required=True, regex='^5G:mnc[0-9]{3}[.]mcc[0-9]{3}[.]3gppnetwork[.]org$')
    resynchronizationInfo = resynchronization(source='*', required=False)
    ausfInstanceId = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-'\
                                            '[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$')


class sqnNumber(serializers.Serializer):
    sqnScheme = serializers.CharField(required=True)
    sqn = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]*$', max_length=12, min_length=12)
    lastIndexes = serializers.IntegerField(required=False)
    indLength = serializers.IntegerField(required=False)
    difsign = serializers.CharField(required=False)


class authSubscriptionValidator(serializers.Serializer):

    encPermanentKey = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$', max_length=32, min_length=32)
    protectionParameterId = serializers.RegexField(required=False,  regex='^[A-Fa-f0-9]*$')
    authenticationMethod = serializers.CharField(required=True)
    sequenceNumber = sqnNumber(source='*', required=False)
    authenticationManagementField = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$', max_length=4, min_length=4)
    algorithumId = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$')
    encOpkey = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$', max_length=32, min_length=32)
    encTopkey = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$', max_length=32, min_length=32)

class authEvents(serializers.Serializer):

    nfInstanceId = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-'\
                                            '[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$')
    success = serializers.BooleanField(required=True)
    timeStamp = serializers.RegexField(required=True, regex='^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z|' \
                                       '[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{1,10}Z$')
    authType = serializers.CharField(required=True)
    servingNetworkName = serializers.RegexField(required=True, regex='^5G:mnc[0-9]{3}[.]mcc[0-9]{3}[.]3gppnetwork[.]org$')



if __name__ == "__main__":


    d1 = {
          "supportedFeatures": "3f66afa6",
          "servingNetworkName": "5G:mnc480.mcc311.3gppnetwork.org",
          "resynchronizationInfo": {
                  "rand": "31323131353836343132313135383634",
                  "auts": "3132313135383634313231313538"
                },
          "ausfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
    }

    d= {
        "encPermanentKey": "5f1d289c5d354d0a140c2548f5f3e3ba",
        "protectionParameterId": "232a",
        "authenticationMethod": "5G_AKA",
        "sequenceNumber": {
               "sqnScheme" : "NON_TIME_BASED",
               "sqn": "a12bf1234566",
               "lastIndexes": 1,
               "indLength": 1,
               "difsign": "POSITIVE"
                },
        "authenticationManagementField": "8101",
        "algorithumId": "1657",
        "encOpkey": "5f1d289c5d354d0a140c2548f5f3e3ba",
        "encTopkey": "465b5ce8b199b49faa5f0a2ee238a6bc"
        }

    d2 = {
         "nfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
         "success": True,
         "timeStamp": "2020-03-23T07:32:25.989994Z",
#        "timeStamp": "2013-01-29T12:34:56Z",
         "authType": "5G_AKA",
         "servingNetworkName": "5G:mnc480.mcc311.3gppnetwork.org"
        }

    valid_ser = authEvents(data=d2)
    if valid_ser.is_valid():
    #    post_data = valid_ser.validated_data
        print("validation succsess")
    else:
        print(valid_ser.errors)
