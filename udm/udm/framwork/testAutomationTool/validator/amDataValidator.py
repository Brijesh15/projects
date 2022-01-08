from rest_framework import serializers

class forbiddenArea(serializers.Serializer):

    tacs = serializers.ListField(required=False, child = serializers.RegexField(required=True, \
                                      regex='(^[A-Fa-f0-9]{4}$)|(^[A-Fa-f0-9]{6}$)'))
    areaCode = serializers.CharField(required=False)

class serviceAreaRestriction(serializers.Serializer):

    restrictionType = serializers.CharField(required=True)
    areas = serializers.ListField(required=True, child = forbiddenArea())
    maxNumOfTAs = serializers.IntegerField(required=False, min_value=0)
    maxNumOfTAsForNotAllowedAreas = serializers.IntegerField(required=False, min_value=0)

class DefaultSingleNssais(serializers.Serializer):

    sst = serializers.IntegerField(required=True, min_value=0, max_value=255)
    sd = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]{6}$')

class nssai(serializers.Serializer):

    supportedFeatures = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$')
    defaultSingleNssais = serializers.ListField(child=DefaultSingleNssais(), required=False)
    singleNssais = serializers.ListField(child=DefaultSingleNssais(), required=False)

class subscribedUeAmbr(serializers.Serializer):

    uplink = serializers.RegexField(required=True, regex='^\d+(\.\d+)?(bps|Kbps|Mbps|Gbps|Tbps)$')
    downlink = serializers.RegexField(required=True, regex='^\d+(\.\d+)?(bps|Kbps|Mbps|Gbps|Tbps)$')

class accessAndMobilityValidator(serializers.Serializer):

    supportedFeatures = serializers.RegexField(required=False, regex='^[A-Fa-f0-9]*$')
    gpsis = serializers.ListField(required=True, child = serializers.RegexField(required=True, \
                                        regex='^(msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+)$'))
    internalGroupIds = serializers.ListField(required=False, child = serializers.RegexField(required=True, \
                        regex='^([A-Fa-f0-9]{8}-[0-9]{3}-[0-9]{2,3}-([A-Fa-f0-9][A-Fa-f0-9]){1,10})$'))
    subscribedUeAmbr = subscribedUeAmbr(source='*', required=False)
    nssai = nssai(source='*', required=False)
    ratRestrictions = serializers.ListField(required=False, child = serializers.CharField(required=True))
    forbiddenAreas = serializers.ListField(required=True, child = forbiddenArea())
    serviceAreaRestriction = serviceAreaRestriction(source='*', required=False)
    coreNetworkTypeRestrictions = serializers.ListField(required=False, child = serializers.CharField())
    rfspIndex = serializers.IntegerField(required=False, min_value=0, max_value=256)
    subsRegTimer = serializers.IntegerField(required=False)
    mpsPriority = serializers.BooleanField(required=False)
    mcsPriority = serializers.BooleanField(required=False)
    activeTime = serializers.IntegerField(required=False)
    dlPacketCount = serializers.IntegerField(required=False, min_value= -1)
    micoAllowed = serializers.BooleanField(required=False)
    sharedAmDataIds = serializers.ListField(required=True, child = serializers.RegexField(required=True, \
                                 regex='^[0-9]{5,6}-.+$'))
    subscribedDnnList = serializers.ListField(required=False, child = serializers.CharField())
    nssaiInclusionAllowed = serializers.BooleanField(required=False)


if __name__ == "__main__":

    d = {
          "supportedFeatures": "123abc50",
          "gpsis": [
                  1
                ],

          "internalGroupIds": [
                  "12345678-123-34-42",
                ],
          "subscribedUeAmbr": {
                  "uplink": "12.50Kbps",
                  "downlink": "12.50Kbps"
                },
          "nssai": {
                  "supportedFeatures": "123afbcd",
                  "defaultSingleNssais": [
                            {
                                        "sst": 0,
                                        "sd": "a123df"
                                      }
                          ],
                  "singleNssais": [
                            {
                                        "sst": 0,
                                        "sd": "123abc"
                                      }
                          ]
                },
          "ratRestrictions": [
                  "NR",
                  "string"
                ],
          "forbiddenAreas": [
                  {"tacs": ["12af"], "areaCode": "string"},
                  {"tacs": ["12af"], "areaCode": "string"}
                ],
          "serviceAreaRestriction": {
                  "restrictionType": "ALLOWED_AREAS",
                  "areas": [
                       {"tacs": ["12ad"], "areaCode": "string"},
                       {"tacs": ["1daf"], "areaCode": "string"}
                          ],
                  "maxNumOfTAs": 0,
                  "maxNumOfTAsForNotAllowedAreas": 0
                },
          "coreNetworkTypeRestrictions": [
                  "5GC",
                  "EPC"
                ],
          "rfspIndex": 0,
          "subsRegTimer": 0,
          "ueUsageType": 0,
          "mpsPriority": True,
      "mcsPriority": True,
        "activeTime": 0,
          "dlPacketCount": 0,
            "sorInfo": {
                    "ackInd": True,
                    "sorMacIausf": "string",
                    "countersor": "string",
                    "provisioningTime": "2020-03-31T11:39:31.289Z"
                  },
              "upuInfo": {
                      "upuDataList": [
                                None,
                                None
                              ],
                      "upuRegInd": True,
                      "upuAckInd": True,
                      "upuMacIausf": "string",
                      "counterUpu": "string",
                      "provisioningTime": "2020-03-31T11:39:31.289Z"
                    },
                "micoAllowed": True,
                  "sharedAmDataIds": [
                          "12345-."
                        ],
                    "subscribedDnnList": [
                            "string",
                            "string"
                          ],
                      "nssaiInclusionAllowed": False
                      }

    valid_ser = accessAndMobilityValidator(data=d)
    if valid_ser.is_valid():
        print("validation succsess")
    else:
        print(valid_ser.errors)

