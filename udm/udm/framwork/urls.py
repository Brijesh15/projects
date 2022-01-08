"""udm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , re_path, include
from framwork import views
from .testAutomationTool.apiHandler.configUpdate import configurations
#Authentication
from .testAutomationTool.apiHandler.ueAuthentication import ueAuthentication
#ContextManagement
from .testAutomationTool.apiHandler.ueContextManagement import amf3gppAccessReg
#subscriberDataManagement
from .testAutomationTool.apiHandler.subscriberDataManagement import accessAndMobility

urlpatterns = [
    #path('admin/', admin.site.urls),
    #configuration
    path('configuration', configurations.configuration.as_view(), name='configurations'),
    #Authentication
   re_path(r'^nudm-ueau/v1/(?P<supiOrSuci>(imsi-[0-9]{5,15}|nai-.+|suci-(0-[0-9]{3}-[0-9]{2,3}|[1-7]-.+)-[0-9]{1,4}-(0-0-.+|[a-fA-F1-9]-([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])-[a-fA-F0-9]+)|.+))/security-information/generate-auth-data/$', \
           ueAuthentication.generateAuthData.as_view(), name='generateAuthData'),
   re_path(r'^nudm-ueau/v1/(?P<supi>(imsi-[0-9]{5,15}|nai-.+))/auth-events/$', \
           ueAuthentication.authEvents.as_view(), name='auth-events'),
    #ContextManagement
   re_path(r'^nudm-uecm/v1/(?P<ueId>(imsi-[0-9]{5,15}|nai-.+|msisdn-[0-9]{5,15}|extid-[^@]+@[^@]+|.+))/registrations/amf-3gpp-access/$', \
           amf3gppAccessReg.amf3gppAccessRegistraion.as_view(), name='3gppaccessRegistration'),
    #subscriberDataManagement
   re_path(r'^nudm-sdm/v2/(?P<supi>(imsi-[0-9]{5,15}|nai-.+))/am-data/$', \
           accessAndMobility.accessAndMobility.as_view(), name='Access and Mobility'),
]
