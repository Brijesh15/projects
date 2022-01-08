from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import index, room, CreateUserAPIView, login, UserRetrieveUpdateAPIView, testAPIView, resetPassword, collegeView ,collegeModView, branchView, branchretupdesView, facultyView, facultyretupdesView, studentView
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework.urlpatterns import format_suffix_patterns

ROUTER = DefaultRouter()
ROUTER.register(r'student', studentView, basename='ln-languages')

urlpatterns = [
    re_path(r'^api-token-refresh/', refresh_jwt_token),    
    re_path(r'^create/$', CreateUserAPIView.as_view()),
    re_path(r'^login/$', login.as_view()),
    re_path(r'^reset-password/$', resetPassword.as_view()),
    re_path(r'^retrieveUpdate/$', UserRetrieveUpdateAPIView.as_view()),
    re_path(r'^college/$', collegeView.as_view()),
    path('college/<int:pk>/', collegeModView.as_view()),
    re_path(r'^branch/$', branchView.as_view()),
    path('branchretupdesView/<int:pk>', branchretupdesView.as_view()),
    re_path(r'^faculty/$', facultyView.as_view()),
    re_path(r'^facultyretupdes/$', facultyretupdesView.as_view()),
    re_path(r'', include(ROUTER.urls)),
    re_path(r'^$', testAPIView.as_view()),
    path('index', index, name='index'),
    path('<str:room_name>/', room, name='room'),
]
#urlpatterns = format_suffix_patterns(urlpatterns)
