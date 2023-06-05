from datetime import datetime, timedelta
from django.contrib.auth.backends import BaseBackend
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.exceptions import AuthenticationFailed, ParseError
from config import settings
from typing import Optional
from rest_framework import authentication
import jwt

User = get_user_model()

from django.contrib.auth.middleware import AuthenticationMiddleware


# now this is my backend otp
# # what I want us to do right now is to right a login view that has 2 fields: phonenumber, password.
#
class JWTAuthBackend(authentication.TokenAuthentication):
    def authenticate(self, request: Optional[HttpRequest]):
        jwt_token = request.META.get("HTTP_AUTHORIZATION")
        print(jwt_token)
        if jwt_token is None:
            return

        jwt_token = JWTAuthBackend.get_token_from_header(jwt_token)

        try:
            payload = jwt.decode(jwt_token, settings.SECRET_KEY, algorithms=["HS256"])
        except jwt.exceptions.InvalidSignatureError:
            raise AuthenticationFailed("Invalid signature")
        except Exception as e:
            print(e)
            raise ParseError()

        user_identifier = payload.get("user_identifier")
        if user_identifier is None:
            raise AuthenticationFailed("User identifier not found")

        user = User.objects.filter(username=user_identifier).first()
        if user is None:
            user = User.objects.filter(phone_number=user_identifier).first()
            if user is None:
                raise AuthenticationFailed("User not found")
        return user, payload

    @classmethod
    def create_jwt(cls, user: User):
        payload = {
            "id": user.pk,
            "user_identifier": user.username,
            "exp": int(
                (
                    datetime.now()
                    + timedelta(hours=settings.JWT_CONF["TOKEN_LIFETIME_HOURS"])
                ).timestamp()
            ),
            "iat": datetime.now().timestamp(),
            "username": user.username,
            "phone_number": user.phone_number,
        }
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        return jwt_token

    @classmethod
    def get_token_from_header(cls, token):
        token = token.replace("Bearer", "").replace(" ", "")  # clean the token
        return token

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return

    def authenticate_header(self, request):
        return "Bearer"


class JwtMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        jwt_auth = JWTAuthBackend()

        try:
            user_jwt_tuple = jwt_auth.authenticate(request)

            if user_jwt_tuple is not None:
                # Extract User object from tuple returned by authenticate() method
                # (It returns a tuple of 'User' instance and corresponding valid token)

                user, _ = user_jwt_tuple

                # Set this User object as current authenticated User in Request Object.
                request.user = user

        except Exception as e:
            print("JWT Middleware Error: ", str(e))

        response = self.get_response(request)

        return response
