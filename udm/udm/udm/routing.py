from django.urls import path, re_path, include
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import users.routing
from .channelsmiddleware import TokenAuthMiddleware
#from myapp.notification import projectNotification


application = ProtocolTypeRouter(
    {
        # (http->django views is added by default)
        "websocket": TokenAuthMiddleware(
        #"websocket": AuthMiddlewareStack(
        URLRouter(users.routing.websocket_urlpatterns)
            )
        }
    )

