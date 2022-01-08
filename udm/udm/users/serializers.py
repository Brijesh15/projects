# users/serializers.py
from rest_framework import serializers
from django.core.validators import MaxValueValidator
from .models import User, college, branches
from datetime import datetime

class userSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

class createUserSerializer(serializers.ModelSerializer):

    #date_joined = serializers.ReadOnlyField()

    class Meta(object):
        model = User
        #fields = ('id', 'email', 'first_name','last_name', 'date_joined', 'password')
        fields = ('id', 'email', 'first_name','last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class collegeSerializer(serializers.ModelSerializer):
    """
    college serializer
    """
    name = serializers.CharField(max_length=50, allow_blank=False)
    college_code = serializers.IntegerField(max_value=9999, min_value=0)
    address = serializers.CharField(max_length=50, allow_blank=True)
    name = serializers.CharField(max_length=50, allow_blank=False)
    stablished = serializers.SerializerMethodField()

    class Meta:
        model = college
        fields = ["id", "name", "college_code", "address", "college_type", "stablished"]
        
    def get_stablished(self, obj):
        return datetime.now().time()
    """
    def to_representation(self, instance):
        data = super(collegeSerializer, self).to_representation(instance)
        data["name"] = {"name": instance.name, "contact" : 8377096939}
        return data
    """     

class branchSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50, allow_blank=False)
    branch_code = serializers.IntegerField(max_value=9999, min_value=0)

    class Meta:
        model = branches
        fields = ["id", "name", "branch_code", "college_name"]

    def to_representation(self, instance):
        data = super(branchSerializer, self).to_representation(instance)
        data["college_name"] = {"id": instance.college_name.id, "name" : instance.college_name.name}
        return data

class facultySerializer(serializers.ModelSerializer):
    pass


class facultyretupdeseSerializer(serializers.ModelSerializer):
    pass


class studentSerializer(serializers.ModelSerializer):
    pass
