from django.contrib.auth.views import LoginView
from django.shortcuts import render
from apps.user.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.views import LoginView, TemplateView
from apps.shop.views import CategoryMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializer import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics

class UserLoginView(CategoryMixin, TemplateView):
    template_name = 'registration/login.html'


class TokenObtainPairViewNew(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self,*args, **kwargs):
        
        username = self.request.POST.get('username')
        passowrd = self.request.POST.get('passowrd')
        user = authenticate(username=username, passowrd=passowrd)
        response = super().post(self.request, *args, **kwargs)
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


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
