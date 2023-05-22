from django.contrib.auth.views import LoginView
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from django.contrib.auth.views import LoginView, TemplateView
from apps.shop.views import CategoryMixin


class UserLoginView(CategoryMixin, TemplateView):
    template_name = 'registration/login.html'


class TokenObtainPairViewNew(TokenObtainPairView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data.get('refresh')
        access_token = response.data.get('access')

        if refresh_token and access_token:
            response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
        return response
