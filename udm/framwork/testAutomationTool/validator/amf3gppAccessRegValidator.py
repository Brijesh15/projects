from rest_framework import serializers


class additionalProp(serializers.Serializer):

    pgwFqdn = serializers.CharField(required=True)
    smfInstanceId = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-'\
                                            '[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$')

class epsIwkPgws(serializers.Serializer):

    additionalProp = additionalProp(source='*', required=False)


class epsInterworkingInfo(serializers.Serializer):

    epsIwkPgws = epsIwkPgws(source='*', required=False)


class plmnId(serializers.Serializer):

    mcc = serializers.CharField(required=True)
    mnc = serializers.CharField(required=True)


class guami(serializers.Serializer):

    plmnId = plmnId(source='*', required=True)
    amfId = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]*$', max_length=6, min_length=6)


class backupAmfInfo(serializers.Serializer):

    backupAmf = serializers.CharField(required=True)
    guamiList = serializers.ListField(child=guami(), required=True)


class amf3gppAccessRegValidator(serializers.Serializer):

    amfInstanceId = serializers.RegexField(required=True, regex='^[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-'\
                                            '[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$')
    supportedFeatures = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$')
    purgeFlag = serializers.BooleanField(required=False)
    pei = serializers.RegexField(required=False, regex='^(imei-[0-9]{15}|imeisv-[0-9]{16}|.+)$')
    imsVoPs = serializers.CharField(required=False)
    deregCallbackUri = serializers.CharField(required=True)
    amfServiceNameDereg = serializers.CharField(required=False)
    pcscfRestorationCallbackUri = serializers.CharField(required=False)
    amfServiceNamePcscfRest = serializers.CharField(required=False)
    initialRegistrationInd = serializers.BooleanField(required=False)
    guami = guami(source='*', required=True)
    backupAmfInfo = serializers.ListField(child=backupAmfInfo(), required=False)

    drFlag = serializers.BooleanField(required=False)
    ratType = serializers.CharField(required=True)
    urrpIndicator = serializers.BooleanField(required=False)
    amfEeSubscriptionId = serializers.CharField(required=False)
    epsInterworkingInfo = epsInterworkingInfo(source='*', required=False)


if __name__ == "__main__":


    d = {
          "amfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
          "supportedFeatures": "12afc430",
          "purgeFlag": True,
          "pei": "string",
          "imsVoPs":"HOMOGENEOUS_SUPPORT",
          "deregCallbackUri": "string",
          "amfServiceNameDereg" : "nnrf-nfm",
          "pcscfRestorationCallbackUri": "string",
          "amfServiceNamePcscfRest":"nnrf-nfm",
          "initialRegistrationInd": True,

          "guami": {
                  "plmnId": {
                            "mcc": "311",
                            "mnc": "480"
                          },
                  "amfId": "12cfd2"
                },
          "backupAmfInfo": [
                  {
                            "backupAmf": "string",
                            "guamiList": [
                                        {
                                                      "plmnId": {
                                                                      "mcc": "311",
                                                                      "mnc": "479"
                                                                    },
                                                      "amfId": "123da0"
                                                    }
                                      ]
                          }
                ],
          "drFlag": True,
          "ratType": "NR",
          "urrpIndicator": True,
          "amfEeSubscriptionId": "string",
          "epsInterworkingInfo": {
                  "epsIwkPgws": {
                            "additionalProp1": {
                                        "pgwFqdn": "string",
                                        "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                                      },
                            "additionalProp2": {
                                        "pgwFqdn": "string",
                                        "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                                      },
                            "additionalProp3": {
                                        "pgwFqdn": "string",
                                        "smfInstanceId": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
                                      }
                          }
                }
         }


    valid_ser = amf3gppAccessRegValidator(data=d)
    if valid_ser.is_valid():
    #    post_data = valid_ser.validated_data
        print("validation succsess")
    else:
        print(valid_ser.errors)
