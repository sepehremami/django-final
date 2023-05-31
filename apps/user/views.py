from django.contrib.auth.views import LoginView
from django.shortcuts import render
from apps.user.backends import JWTAuthBackend
from apps.user.models import User, Address
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.views import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from .serializers import ObtainTokenSerializer, UserSerializer, AddressSerializer
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions, views as api_views
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes, api_view
from rest_framework.authentication import SessionAuthentication
from rest_framework.authtoken.views import ObtainAuthToken


User = get_user_model()


class UserLoginView(TemplateView):
    template_name = "registration/login.html"


class TokenObtainPairViewNew(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]

    def post(self, *args, **kwargs):
        username = self.request.POST.get("username")
        passowrd = self.request.POST.get("passowrd")
        response = super().post(self.request, *args, **kwargs)
        user = authenticate(username=username, passowrd=passowrd)
        if user is not None:
            login(self.request, user)
        refresh_token = response.data.get("refresh")
        access_token = response.data.get("access")

        if refresh_token and access_token:
            response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
        return response


class ProfileView(TemplateView):
    model = User
    template_name = "user/profile.html"


class ObtainTokenView(ObtainAuthToken):
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer: ObtainTokenSerializer = self.serializer_class(data=request.data,  context={'request': request})
        serializer.is_valid(raise_exception=True)

        username_or_phone = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user = User.objects.get(username=username_or_phone)
        if user is None or not user.check_password(password):
            return Response({"message": "Invalid Credentials"})

        jwt_token = JWTAuthBackend.create_jwt(user)

        return Response({"token": jwt_token})


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def index(request):
    if request.user:
        return Response(f"Responseyou name is {request.user.username}")
    return Response("failed!")


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    def get_queryset(self):
        """
        Return a queryset of all addresses for the authenticated user.
        """
        if isinstance(self.request.user,User):
            return Address.objects.filter(user=self.request.user)