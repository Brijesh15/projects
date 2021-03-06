from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
from .models import *
import os

class FrontendAppView(View, HomePageView):

    def get(self, request):

        try:
            self.insertData()
            print("settings.REACT_APP_DIR",settings.REACT_APP_DIR)
            with open(os.path.join(settings.REACT_APP_DIR, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse("""This URL is only used when you have built the production  version of the app. Visit \
                                http://localhost:3000/ instead, or run `yarn run build` to test the production version. \
                                 """, status=501,)
