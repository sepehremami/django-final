from django.contrib.auth.views import LoginView
from django.shortcuts import render
from apps.user.backends import JWTAuthBackend
from apps.user.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.views import TemplateView
from apps.shop.views import CategoryMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from .serializers import ObtainTokenSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions, views as api_views
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login
User = get_user_model()

class UserLoginView(CategoryMixin, TemplateView):
    template_name = 'registration/login.html'


class TokenObtainPairViewNew(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        
        username = self.request.POST.get('username')
        passowrd = self.request.POST.get('passowrd')
        response = super().post(self.request, *args, **kwargs)
        user = authenticate(username=username, passowrd=passowrd)
        if user is not None:
            login(self.request, user)
        refresh_token = response.data.get('refresh')
        access_token = response.data.get('access')

        if refresh_token and access_token:
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = "user/profile.html"



class ObtainTokenView(api_views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer:ObtainTokenSerializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_phone = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = User.objects.get(username=username_or_phone)
        # if user is None:
        #     user = User.objects.get(phone_number=username_or_phone)
        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid Credentials'})
        
        jwt_token = JWTAuthBackend.create_jwt(user)
        
        return Response({'access':jwt_token})


def index(request:HttpRequest, *args, **kwargs):
    user = authenticate(request=request)
    print(user)
    if user:
        login(request, user, backend='apps.user.backends.JWTAUTHBackend')
        return HttpResponse(f'you name is {user.username}')
    # print(payload)
    return HttpResponse('failed!')




