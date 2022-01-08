from django.urls import re_path

from .notification import ChatConsumer, projectNotification

websocket_urlpatterns = [
        #re_path(r'ws/user/(?P<room_name>\w+)/$', ChatConsumer),
        re_path(r'ws/user/(?P<room_name>\w+)/$', projectNotification),
        ]
