from django.db import close_old_connections
from django.contrib.auth.models import AnonymousUser
#from rest_framework_simplejwt.tokens import UntypedToken
#from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs


class TokenAuthMiddleware:
    """
    Custom token auth middleware
    """

    def __init__(self, inner):
        # Store the ASGI application we were passed
        self.inner = inner

    def __call__(self, scope):

        close_old_connections()
        try:
            token = parse_qs(scope["query_string"].decode("utf8"))["token"][0]
        except:
            #user = AnonymousUser()
            print("ananymous user")
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(decoded_data)
            user = get_user_model().objects.get(id=decoded_data["user_id"])

        return self.inner(dict(scope, user=user))

