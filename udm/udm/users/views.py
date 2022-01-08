import time
import datetime
import traceback
import random
import string
from django.shortcuts import render
from django.core.mail import send_mail
from django_filters import rest_framework as filters
from django.contrib.auth import authenticate, logout
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import userSerializer, createUserSerializer, collegeSerializer, branchSerializer, facultySerializer, facultyretupdeseSerializer, studentSerializer
from rest_framework_jwt.settings import api_settings
from .filter import userFilters
from rest_framework.response import Response
from rest_framework import status
from .models import User, college, branches, faculty, student
from rest_framework_jwt.utils import jwt_payload_handler
import jwt
from django.conf import settings

# users/views.py

def index(request):
    print("brijesh print index.html")
    return render(request, 'users/index.html', {})

def room(request, room_name):
    return render(request, 'users/room.html', {
        'room_name': room_name
    })

class CreateUserAPIView(ListAPIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
    serializer_class = createUserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = userFilters

    def get_queryset(self):
        return User.objects.all()
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class login(GenericAPIView):

    permission_classes = (AllowAny,)
    serializer_class = userSerializer
    def post(self, request):
        try: 
            print(request.data)
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                print(serializer.data)
                email = serializer.data.get('email')
                password = serializer.data.get('password')
                try:
                    user = User.objects.get(email=email, password=password)
                except:
                    return Response({'error':'user does not exist, please signup first'} ,\
                                    content_type='application/json', status=status.HTTP_401_UNAUTHORIZED)
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['token'] = token
                return Response(user_details, content_type='application/json', status=status.HTTP_200_OK)
            return Response(serializer.errors, content_type='application/json',\
                                        status=status.HTTP_400_BAD_REQUEST)
        except:
            print(traceback.format_exc())
            res = {}
            return Response(res, content_type='application/json', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
     
    # Allow only authenticated users to access this url
    #authorizarion_class = TokenAuthentication
    #permission_classes = (IsAuthenticated,)
    serializer_class = userSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        print("kfewjfj",request.user)
        serializer = self.serializer_class(request.user)
                                 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
                 
        serializer = UserSerializer(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                                          
        return Response(serializer.data, status=status.HTTP_200_OK)

class resetPassword(APIView):

    permission_classes = []
    
    def randomString(self, stringLength=8):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def put(self, request):
        try:
            newPass = self.randomString()
            send_mail(
                'Reset password',
                newPass,
                'aricent.havoc@gmail.com',
                ['aricent.havoc@gmail.com'],
                fail_silently=False,
            )
        except:
            print("error",traceback.format_exc())

            return Response({"error":"Error in password reset"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"response":"password has been reset"}, status=status.HTTP_200_OK)


class testAPIView(APIView):
     
    #authorizarion_class = []
    #permission_classes = (IsAuthenticated,)
    #permission_classes = []

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        print("printing from test API")
        serializer = {"test": "testAPIView"}
                                 
        return Response(serializer, status=status.HTTP_200_OK)

#class collegeView(GenericAPIView):
class collegeView(APIView):
    """
    college class
    """
    #serializer_class = collegeSerializer

    def get(self, request):
        college_data = college.objects.all()
        serializer = collegeSerializer(college_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = collegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#class collegeModView(GenericAPIView):
class collegeModView(APIView):

#    serializer_class = collegeSerializer

    def get(self, request, pk):
        try:
            college_data = college.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = collegeSerializer(college_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            college_data = college.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = collegeSerializer(college_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            college_data = college.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = collegeSerializer(college_data)
        college_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        pass


class branchView(generics.ListCreateAPIView):
    """
    branch class
    """
    queryset = branches.objects.all()
    serializer_class = branchSerializer


class branchretupdesView(generics.RetrieveUpdateDestroyAPIView):
    """
    branch class
    """
    queryset = branches.objects.all()
    serializer_class = branchSerializer


class facultyView(generics.ListCreateAPIView):
    """
    faculty class
    """

class facultyretupdesView(generics.RetrieveUpdateDestroyAPIView):
    """
    faculty class
    """

class studentView(viewsets.ModelViewSet):
    """
    student class
    """

