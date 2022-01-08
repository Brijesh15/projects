from .models import User
import django_filters
from django_filters import rest_framework as filters

class userFilters(filters.FilterSet):

    #first_name = django_filters.CharFilter()

    class Meta:
        model = User
        #fields = ['email']
        fields = {'email': ['exact'],}
